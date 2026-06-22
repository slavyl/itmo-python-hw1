D = {"food": "Apple", "quantity": 4, "color": "Red"}

print("Исходный словарь:", D)
print("Значение по ключу food:", D["food"])

D["quantity"] += 10

print("После изменения quantity:", D)

dp = {}

dp["name"] = input("Введите имя: ")
dp["age"] = int(input("Введите возраст: "))

print("Новый словарь:", dp)