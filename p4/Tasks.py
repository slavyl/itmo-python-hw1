##Упражнение 1
# n = int(input('Задайте число '))
# k = 0
# while n > 0: # Прекратить действия, когда n станет 0
#     n = n //10 # Отбрасывание последней цифры числа n
#     k = k + 1 # Увеличение значения переменной-счетчика
# print("Количество цифр в числе", k)

##Контрольное задание к Упр 1
# n = int(input('Задайте число '))
# k = 0
# s = 0
# while n > 0:
#     s = s + n % 10
#     n = n // 10
#     k = k + 1
# print("Количество цифр в числе", k)
# print("Сумма цифр числа", s)



##Упражнение 2
# a = int(input('Задайте первое число '))
# b = int(input('Задайте второе число '))
# while a != b:
#     if a > b:
#         a = a - b
#     else:
#         b = b - a
# nod = a
# print('НОД равен', nod)



##Упражнение 3
# from random import randint   # подключение функции из модуля random
# total = 100                  # запас ресурса
# i = 0                        # счетчик итераций цикла
# while i < 5:
#     n = randint(1, 50)  #имитация расхода ресурса
#     total = total - n
#     if total < 0:
#         total = 0
#         break
#     i = i + 1
# else:
#     print("Процесс выполнен полностью")
#
# print("Осталось", total)

##Контрольное задание
# from random import randint
#
# total = 100
#
# for stage in range(5):
#     n = randint(1, 50)
#     print(f"Этап {stage + 1}. Расход ресурса: {n}")
#
#     total -= n
#
#     if total < 0:
#         total = 0
#         print("Ресурс закончился. Процесс остановлен досрочно.")
#         break
# else:
#     print("Процесс выполнен полностью")
#
# print("Осталось ресурса:", total)



##Упражнение 4
# num = input('Введите число для подсчета суммы цифр: ')
# sumIt = 0
# for it in num:
#     sumIt += int(it)
# print(f"Сумма цифр числа {num} равна {sumIt}")


