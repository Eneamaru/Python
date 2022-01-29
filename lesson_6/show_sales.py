from sys import argv
from sys import exit

if len(argv) == 1:
    with open('bakery.csv', 'r', encoding='utf-8') as f:
        print(f.read())
elif len(argv) == 2:
    with open('bakery.csv', 'r', encoding='utf-8') as f:
        print(f.read().splitlines()[int(argv[1]):])
elif len(argv) == 3:
    with open('bakery.csv', 'r', encoding='utf-8') as f:
        print(f.read().splitlines()[int(argv[1]):int(argv[2]) + 1])
else:
    exit(1)