from sys import argv

value = argv[1]

with open('bakery.csv', 'a', encoding='utf-8') as f:
    f.write(f'{value}\n')