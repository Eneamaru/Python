duration = int(input("Введите количество секунд: "))

if duration < 60:  # если секунд меньше 60
    print(duration, "сек")
elif 60 <= duration < 3600:  # если секунд от 60 до 3599
    minutes = duration // 60
    seconds = duration % 60
    print(minutes, "мин", seconds, "сек")
elif 3600 <= duration < 86400:  # если секунд от 3600 до 86399
    hours = duration // 3600
    minutes = (duration % 3600) // 60
    seconds = (duration % 3600) % 60
    print(hours, "час", minutes, "мин", seconds, "сек")
else:
    days = duration // 86400  # во всех остальных случаях
    hours = (duration % 86400) // 3600
    minutes = ((duration % 86400) % 3600) // 60
    seconds = ((duration % 86400) % 3600) % 60
    print(days, "дн", hours, "час", minutes, "мин", seconds, "сек")
