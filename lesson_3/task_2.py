def num_translate(key):
    """Translate numbers from 0 to 10"""
    numbers = {'zero': 'ноль', 'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре', 'five': 'пять',
               'six': 'шесть', 'seven': 'семь', 'eight': 'восемь', 'nine': 'девять', 'ten': 'десять'}
    if key.islower():
        print(numbers.get(key))
    else:
        print(numbers.get(key.lower()).capitalize())


a = num_translate(input('Введите число на английском от 0 до 10: '))
