min = 1
max = 10
number = int(input(f'Загадайте число от {min} до {max}: '))

if number < min:
    number = min

print(f'Вы загадали {number}')
