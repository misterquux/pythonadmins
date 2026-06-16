from pprint import pprint

address_list = [
    (
        "salutation",
        "first_name",
        "last_name",
        "street",
        "city",
    ),
    (
        "Mr.",
        "Frodo",
        "Baggins",
        "Bag End 1",
        "Hobbiton",
    ),
    (
        "Mr.",
        "Samwise",
        "Gamgee",
        "Bagshot Row 2",
        "Hobbiton",
    ),
    (
        "Mrs.",
        "Galadriel",
        "of Lothlorien",
        "189 Flower Gardens",
        "Lothlorien",
    ),
]


def get_address_dict(address_list: list[tuple]) -> dict:
    """Transformiere Liste mit Tupeln in ein Dict."""
    head = address_list.pop(0)
    address_dict = {}
    for row in address_list:
        address_dict[row[1]] = dict(zip(head, row))
    return address_dict


address_dict = get_address_dict(address_list)
pprint(address_dict, depth=2)
print(address_dict["Frodo"])
print(address_dict["Frodo"]["street"])
print(address_dict["Frodo"]["last_name"])
