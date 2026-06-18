# Funktionsparameter
Parameter definieren und Argumente übergeben

## Positionelle Argumente
Die Argumente werden der Position nach übergeben.

    def summe(a, b, c):
        d = a + b + c

    summe(3, 4, 5)


## Default Werte
Wir können in einer Funktion auch Default-Werte für eine Funktion definieren. Bei Aufruf dieser Funktion ist es nicht nötig, dieses Argument zu übergeben. Wenn es aber übergeben wird, überschreibt es den Default-Wert. Wichtig ist, dass sie nach den positionellen Parametern definiert werden.

    def func(a, b, c=2):
        print(a, b, c)

    func(1, 2) => 1, 2, 2
    func(1, 2, 9) => 1, 2, 9

## Unbestimmte Anzahl an Argumenten
Eine unbestimmte Anzahl an Argumenten kann mit dem Sternchen-Operator (Asterisk) aufgefangen werden.  Wir erhalten einen Tupel.

    def summe(*args):
        sum(args)

    summe(1, 4, 6)


    def fixed(a, b, *args):
        print(a, b)

    fixed(1, 4, 6, 7, 9)

## Positionelle Argumente erzwingen
Wir können im Parameterkopf definieren, dass für gewisse Parameter ein Aufruf nur über positionelle Argumente möglich ist. Dazu kann man das Slash-Zeichen nutzen um zu bestimmen, dass alles VOR dem Zeichen via Position übergeben muss.

    def func(a, b, /, c):
        print(a, b, c)

    func(a=3, b=4, c=5) Fehler!
    func(3, 4, c=5) Richtig!

## Keyword Argumente
Es ist auch möglich, eine Funktion mit Keyword-Argument aufzurufen. Der Parametername entspricht dabei dem Keywort. Beachte, dass beim Aufruf der Funktion die Reihenfolge der Argumente keine Rolle spielt.

    def set_encoding(encoding, filename):
    settings = encoding

    set_encoding(filename='p.jpg', encoding='utf-8')

## Unbestimmte Anzahl an Keyword Argumenten

Eine unbestimmte Anzahl an Keyword-Argumenten kann mit dem **Doppelten-Sternchen-Operator (Asterisk) aufgefangen werden. Wir erhalten ein Dictionary.

    def say_hello(**kwargs):
        for key, value in kwargs.items():
                    print(key, value)
say_hello(city="London", country="UK")


## Keyword Args erzwingen
Es ist möglich, eine Funktion so zu definieren, dass sie nur mit  Keyword-Argument aufgerufen werden kann. Dazu können wir den Sternchen-Operator (Asterisk) nutzen.

    def connect_to_db(*, username, password, database):
         …

    connect_to_db(username='bernd', password='supersecure', database='main')
