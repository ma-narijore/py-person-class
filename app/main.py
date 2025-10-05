class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    # 1️⃣ Створюємо всіх людей
    for pers in people:
        Person(pers["name"], pers["age"])

    # 2️⃣ Встановлюємо зв’язки
    for pers in people:
        person = Person.people[pers["name"]]

        # якщо є дружина — встановлюємо
        if "wife" in pers and pers["wife"]:
            person.wife = Person.people.get(pers["wife"])
            Person.people[pers["wife"]].husband = person

        # якщо є чоловік — встановлюємо
        if "husband" in pers and pers["husband"]:
            person.husband = Person.people.get(pers["husband"])
            Person.people[pers["husband"]].wife = person

    # 3️⃣ Повертаємо список
    return list(Person.people.values())


# people = [
#     {"name": "Ross", "age": 30, "wife": "Rachel"},
#     {"name": "Joey", "age": 29, "wife": None},
#     {"name": "Phoebe", "age": 31, "husband": None},
#     {"name": "Chandler", "age": 30, "wife": "Monica"},
#     {"name": "Monica", "age": 32, "husband": "Chandler"},
#     {"name": "Rachel", "age": 28, "husband": "Ross"},
# ]
#
# person_list = create_person_list(people)
#
# print(person_list[0].__dict__)
