distorted = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']

for i in distorted:
    distorted = (i.split(' ')[-1]).title()
    print(f'Привет, {distorted}!')
