# Сгенерируйте список на 30 элементов. Отсортируйте список по возрастанию, методом сортировки выбором.
from random import randint

list30elem = [randint(1, 100) for _ in range(30)]
print("Сгенерированный список:", list30elem)
for i in range(len(list30elem) - 1):
    min = i
    for k in range(i + 1, len(list30elem)):
        if list30elem[k] < list30elem[min]:
            min = k
    list30elem[i], list30elem[min] = list30elem[min], list30elem[i]
print("Отсортированный список:", list30elem)