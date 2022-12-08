# 2) Написать программу, которая генерирует двумерный массив на A x B элементов ( A и B вводим с клавиатуры)
# И считаем средне-арифметическое каждой строки (не пользуемся встроенными методами подсчета суммы)

a = int(input('Введите размер A: '))
b = int(input('Введите размер B: '))
from random import randint
listmass = [0] * a
for i in range(a):
    listmass[i] = [0] * b
for i in range(a):
    for j in range(b):
        listmass[i][j] = randint(0, a * b * 2)
print('Сгенерированный двумерный массив:')
for i in range(a):
    print(listmass[i])
for i in range(a):
    middle = 0
    for j in range(b):
        middle += listmass[i][j]
    middle = middle/b
    print(f'Среднее арифметическое {i+1}-ой строки: {middle}')

