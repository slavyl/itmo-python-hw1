zakaz_sum = float(input("Введите сумму заказа в ресторане:\n"))

nalog_sum = 0.40
chai_sum = 0.10

nalog = zakaz_sum * nalog_sum
chai = zakaz_sum * chai_sum
total = zakaz_sum + nalog + chai

print("Сумма заказа: {:.2f}" .format(zakaz_sum))
print("Сумма налога: {:.2f}" .format(nalog))
print("Сумма чаевых: {:.2f}" .format(chai))
print("Сумма заказа: {:.2f}" .format(total))