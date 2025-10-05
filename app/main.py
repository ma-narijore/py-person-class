class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    # 1️⃣ Створюємо всіх людей
    for person_dict in people:
        Person(person_dict["name"], person_dict["age"])

    # 2️⃣ Встановлюємо зв’язки
    for person_dict in people:
        person = Person.people[person_dict["name"]]

        # якщо є дружина — встановлюємо
        if "wife" in person_dict and person_dict["wife"]:
            person.wife = Person.people.get(person_dict["wife"])
            Person.people[person_dict["wife"]].husband = person

        # якщо є чоловік — встановлюємо
        if "husband" in person_dict and person_dict["husband"]:
            person.husband = Person.people.get(person_dict["husband"])
            Person.people[person_dict["husband"]].wife = person

    # 3️⃣ Повертаємо список
    return [Person.people[d.get("name")] for d in people]


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
