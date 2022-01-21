from random import choice

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

def get_jokes(x):
    """Prints random jokes to the console in the amount specified by the user"""
    for i in range(x):
        print(f'{choice(nouns)} {choice(adverbs)} {choice(adjectives)}')


get_jokes(int(input('Введите количство шуток: ')))
