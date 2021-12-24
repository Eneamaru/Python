perc = 0

while perc < 101:
    if perc % 10 == 1 and perc != 11:
        print(perc, "процент")
    elif (perc % 10 == 2 or perc % 10 == 3 or perc % 10 == 4) and perc != 12 and perc != 13 and perc != 14:
        print(perc, "процента")
    else:
        print(perc, "процентов")
    perc += 1
