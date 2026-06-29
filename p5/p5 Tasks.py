## Упражнение 1
# fruits = ["Apple", "Grape", "Peach", "Banan", "Orange"]
#
# print(fruits[0])
# print(fruits[1])
# print(fruits[4])
# print(fruits[-1])
#
# fruits[0] = "Watermelon"
# fruits[3] = "Lemon"
#
# fruits.append("Banan")
#
# if "Apple" in fruits:
#     print("В списке есть элемент Apple")
# else:
#     print("В списке нет элемента Apple")
#
# print(fruits)



## Упражнение 2
# s = "ab12c59p7dq"
#
# digits = []
#
# for symbol in s:
#     if "1234567890".find(symbol) != -1:
#         digits.append(int(symbol))
#
# print(digits)



## Упражнение 3
# user1 = {
#     "firstname": "Иван",
#     "lastname": "Петров",
#     "age": 19,
# }
#
# print(user1)
#
# fname = input("Введите имя: ")
# lname = input("Введите фамилию: ")
# age = int(input("Введите возраст: "))
#
# user2 = dict(
#     firstname=fname,
#     lastname=lname,
#     age=age,
# )
#
# print(user2)
#
# users = []
#
# users.append(user1)
# users.append(user2)
#
# print(users)



## Упражнение 4.1
sales = []

days = [
    "Понедельник",
    "Вторник",
    "Среда",
    "Четверг",
    "Пятница",
    "Суббота",
    "Воскресенье",
]

for day in days:
    money = float(input(f"{day}: "))
    sales.append(money)

total = sum(sales)

print(f"\nОбщий объем продаж за неделю: {total}")

sales.sort()

print("\nПродажи по возрастанию:")

for sale in sales:
    print(sale)