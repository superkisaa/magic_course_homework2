# Задайте список из вещественных чисел.
# Напишите программу, которая найдёт разницу между
# максимальным и минимальным значением дробной части элементов.
#  Пример:
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19

numbers = [1.1, 1.2, 3.1, 5, 10.01]
spisok = []
for i in numbers:
    i = str(i)
    spisok.append(i.split('.'))
num_spisok = []
for j in spisok:
    if len(j) == 1:
        continue
    else:
        num_spisok.append(j[1])
min = num_spisok[0]
for num in num_spisok:
    if int(num) < min:
        min = int(num)
    else:
        continue
max = num_spisok[0]
for num1 in num_spisok:
    if int(num1) > max:
        max = int(num1)
    else:
        continue
res = max - min
print(res)


