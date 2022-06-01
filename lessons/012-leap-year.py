year = int(input('Введите год: '))
leap = 'високосный'
regular = 'обычный'

if year % 4 != 0:
    print(regular)

elif year % 100 == 0:
    if year % 400 == 0:
        print(leap)
    else:
        print(regular)

else:
    print(leap)
