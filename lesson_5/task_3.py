def gen(a, b):
    """sequentially concatenates elements from two lists into a tuple"""
    _a = (el for el in a)
    _b = (el for el in b)
    for i in zip(_b, _a):
        yield i[::-1]
    for rest in _a:
        yield rest, None


tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена', 'Мария', 'Анна']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']

school = gen(tutors, klasses)

for item in school:
    print(item)


