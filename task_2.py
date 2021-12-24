num_lst_1 = []  # Список состоящий из кубов нечётных чисел от 1 до 1000
num_lst_2 = []  # Список состоящий из чисел списка num_lst1, сумма цифр которых, делится на ноль без остатка
num_lst_3 = []  # Список состоящий из чисел списка num_lst1, к которым было прибавлено 17
num_lst_4 = []  # Список состоящий из чисел списка num_lst3, сумма цифр которых, делится на ноль без остатка

for i in (range(1, 1000, 2)):
    num_lst_1.append(i ** 3)

#  print(num_lst_1)

for i in num_lst_1:
    digit_sum_1 = 0
    for digit_1 in str(i):
        digit_sum_1 += int(digit_1)
    if digit_sum_1 % 7 == 0:
        num_lst_2.append(i)
num_sum_1 = 0
for i in num_lst_2:
    num_sum_1 += i

#  print(num_lst_2)

print(num_sum_1)

for i in num_lst_1:
    seventeen = i + 17
    num_lst_3.append(seventeen)

#  print(num_lst_3)

for i in num_lst_3:
    digit_sum_2 = 0
    for digit_2 in str(i):
        digit_sum_2 += int(digit_2)
    if digit_sum_2 % 7 == 0:
        num_lst_4.append(i)
num_sum_2 = 0
for i in num_lst_4:
    num_sum_2 += i

#  print(num_lst_4)

print(num_sum_2)
