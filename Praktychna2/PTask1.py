'''
Дано список чисел. Порахувати скільки в ньому пар чисел (тобто
два однакових числа утворюють пару) .
Наприклад:
1 2 3 5 3 2 Результат має бути: 2
'''


def count(l, numb):
    c = 0
    for i in l:
        if i == numb:
            c += 1
    return c


l_numb = [3, 4, 4, 4, 3, 3, 2, 1, 5, 7, 7, 4, 4, 4]
rez = {}
for i in l_numb:
    if i not in rez.keys():
        rez[i] = count(l_numb, i)
pary = 0
for k in rez.keys():
    print(str(k) + ' утворює ' + str(rez[k] // 2) + ' пари')
    pary += rez[k] // 2
print('Загалом в списку ' + str(pary) + ' пар')
