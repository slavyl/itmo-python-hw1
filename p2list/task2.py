seq = (2, 8, 23, 97, 92, 44, 17, 39, 11, 12)

print("Кортеж:", seq)
print("Сколько раз встречается 8:", seq.count(8))
print("Индекс элемента 44:", seq.index(44))

listseq = list(seq)

print("Преобразованный список:", listseq)
print("Тип listseq:", type(listseq))

listseq.append(100)
listseq.insert(1, 500)
listseq.remove(23)
listseq.reverse()

print("После применения методов списка:", listseq)