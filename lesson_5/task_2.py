n = int(input('Введите целое число: '))
nums_gen = (num for num in range(1, n + 1, 2))
for i in nums_gen:
    print(i)
