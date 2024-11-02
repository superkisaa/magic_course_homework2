# В большой текстовой строке подсчитать
# количество встречаемых слов и вернуть 10 самых частых.
# Не учитывать знаки препинания и регистр символов.

str = input()
new_str = str.lower()
words = new_str.split(' ')
a = {}
for i in words:
    if i != ',':
        if i in a:
            a[i] += 1
        else:
            a[i] = 1

sorted_a = sorted(a.items(), key=lambda item: item[1], reverse=True)
spisok = []
if len(sorted_a) <= 10:
    for i in range(len(sorted_a)):
        spisok.append(sorted_a[i][0])
else:
    for i in range(10):
        spisok.append(sorted_a[i][0])
print(spisok)







