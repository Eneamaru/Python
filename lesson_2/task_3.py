lst = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

print(lst)
for i in lst:  # находим и форматируем числа в списке
    if i.isdigit():
        num = int(i)
        num = f'{num:02d}'
        lst.insert(lst.index(i), num)
        lst.remove(i)
    elif i.lstrip('+').isdigit():  # если число со знаком '+'
        num = int(i)
        num = f'+{num:02d}'
        lst.insert(lst.index(i), num)
        lst.remove(i)
    elif i.lstrip('-').isdigit():  # если число со знаком '-'
        num = int(i)
        num = f'-{num:02d}'
        lst.insert(lst.index(i), num)
        lst.remove(i)

num = 0

for i in lst:  # обособляем целые числа кавычками
    if i.lstrip('-+').isdigit():
        if num == i:
            continue
        num = i
        lst.insert(lst.index(i), '"')
        lst.insert(lst.index(i) + 1, '"')

num_2 = 0

for i in lst:
    if i.lstrip('+').isdigit():
        if num_2 == i:
            continue
        num_2 = '"' + i + '"'
        lst.insert(lst.index(i), num_2)
        lst.remove(i)

while '"' in lst:
    lst.remove('"')

print(lst)

msg = ' '.join(lst)

print(msg)
