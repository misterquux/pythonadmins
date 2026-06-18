from pathlib import Path

DATA_FILE = Path(__file__).parent / "trump_speeches.txt"


def read_text() -> str:
    """Lese die Datei ein und liefere den eingelesenen String."""
    with open(DATA_FILE, encoding="utf-8") as f:
        return f.read()


def sentence_mode(text: str, search_word: str) -> None:
    """Liefere alle Sätze die mit Punkt enden."""
    sentences = text.split(".")

    for sentence in sentences:
        sentence = sentence.strip()

        if search_word in sentence:
            print(sentence)
            print("-" * 50)


def word_mode(text: str, search_word: str) -> None:
    """Finde alle Wörter, mit search_word am Anfang."""
    result = []
    words = text.split()

    for word in words:
        word = word.strip(".,!?;:\"'()[]")

        if word.startswith(search_word):
            result.append(word)

    # von doppelten befreien via set(). sortieren via sorted()
    result = sorted(set(result))

    print(result)


def top_mode(text: str) -> None:
    """Berechne die 10 Ten Wort-Nennungen"""
    counter = {}
    words = text.split()

    for word in words:
        word = word.strip(".,!?;:\"'()[]").lower()

        if len(word) <= 5:
            continue

        if word in counter:
            counter[word] += 1
        else:
            counter[word] = 1

    top_ten = sorted(
        counter.items(),
        key=lambda item: item[1],
        reverse=True,
    )[:10]

    print(top_ten)


def main() -> None:
    text = read_text()
    while True:
        user_input = input("Eingabe (SEN <wort>, WORD <wort>, TOP, exit): ").strip()

        parts = user_input.split(maxsplit=1)
        mode = parts[0].upper()

        if mode == "EXIT":
            print("Goodbye")
            return

        if mode == "SEN":
            if len(parts) != 2:
                print("Bitte: SEN <SUCHWORT>")
                return
            sentence_mode(text, parts[1])

        elif mode == "WORD":
            if len(parts) != 2:
                print("Bitte: WORD <SUCHWORT>")
                return
            word_mode(text, parts[1])

        elif mode == "TOP":
            top_mode(text)

        else:
            print("Unbekannter Modus.")


if __name__ == "__main__":
    main()
