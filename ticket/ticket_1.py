while True:
    ticket = input("Введите номер своего билета (6 цифр)\n")

    if len(ticket) == 6 and ticket.isdigit():
        break
    print("Введите номер билета еще раз:")

left = int(ticket[0]) + int(ticket[1]) + int(ticket[2])
right = int(ticket[3]) + int(ticket[4]) + int(ticket[5])

if left == right:
    print("Поздравляем, ваш билет - счастливый!")
else:
    print("К сожалению, в этот раз вам не повезло")

