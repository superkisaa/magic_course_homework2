# Напишите программу, которая принимает две строки
# вида “a/b” - дробь с числителем и знаменателем.
# Программа должна возвращать сумму дробей.
# Ввод:
# 1/2
# 2/3
# Вывод:
# 7/6  (будет еще круче если упростите до 1+1/6)

a = input()
b = input()

znam_a = int(a[2])
znam_b = int(b[2])
chis_a = int(a[0])
chis_b = int(b[0])
sum_chis = znam_a*chis_b + znam_b*chis_a
sum_znam = znam_a*znam_b
sum = f"{sum_chis}/{sum_znam}"
print(sum)
