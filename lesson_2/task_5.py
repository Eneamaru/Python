price = [36.7, 58.87, 83, 97.5, 5.38, 49, 15.89, 126.4, 384.56, 297, 5.13, 7.9, 6]

for i in price:
    if i == price[-1]:
        rub = int(i)
        kop = int((i - rub) * 100)
        print(f'{rub} руб {kop:02d} коп', end='.\n')
    else:
        rub = int(i)
        kop = int((i - rub) * 100)
        print(f'{rub} руб {kop:02d} коп', end=', ')

print(id(price))

price.sort()

for i in price:
    if i == price[-1]:
        rub = int(i)
        kop = int((i - rub) * 100)
        print(f'{rub} руб {kop:02d} коп', end='.\n')
    else:
        rub = int(i)
        kop = int((i - rub) * 100)
        print(f'{rub} руб {kop:02d} коп', end=', ')

print(id(price))

reverse = sorted(price, reverse=True)

for i in reverse:
    if i == reverse[-1]:
        rub = int(i)
        kop = int((i - rub) * 100)
        print(f'{rub} руб {kop:02d} коп', end='.\n')
    else:
        rub = int(i)
        kop = int((i - rub) * 100)
        print(f'{rub} руб {kop:02d} коп', end=', ')

#  print(id(reverse))

for i in reverse[4::-1]:
    if i == reverse[0]:
        rub = int(i)
        kop = int((i - rub) * 100)
        print(f'{rub} руб {kop:02d} коп', end='.\n')
        break
    else:
        rub = int(i)
        kop = int((i - rub) * 100)
        print(f'{rub} руб {kop:02d} коп', end=', ')

#  print(id(reverse))
