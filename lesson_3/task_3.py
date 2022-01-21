def thesaurus(*args):
    """Adds names from the list, sorting them by the first letter"""
    dict_names = {}
    for idx in args:
        name = idx
        f_letter = name[0]
        if dict_names.get(f_letter) is None:
            dict_names[f_letter] = [name]
        else:
            dict_names[f_letter].append(name)
    return dict_names


print(thesaurus('Иван', 'Сергей', 'Анна', 'Мария', 'Александр'))
