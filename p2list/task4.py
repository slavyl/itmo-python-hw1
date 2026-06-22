rec = {
    "name": {
        "firstname": "Bob",
        "lastname": "Smith",
    },
    "job": ["dev", "mgr"],
    "age": 25,
}

rec["job"].append("janitor")

print("Полная информация о персоне:")
print(f"Имя: {rec['name']['firstname']}")
print(f"Фамилия: {rec['name']['lastname']}")
print(f"Возраст: {rec['age']}")
print(f"Должности: {', '.join(rec['job'])}")