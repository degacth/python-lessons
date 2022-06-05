from random import randint
from time import time

min_time = 2.0
min = 1
max = 5
lives = 3
points = 0

print('Введи предложенное число за минимальное время')

while True:
    number = randint(min, max)
    start = time()
    answer = int(input(f'{number}: '))
    answer_time = time() - start

    if answer == number and min_time > answer_time:
        points += 10
        print(f'Жизни {lives}, очки {points}')
        continue

    wrong_message = 'Неверный ответ' if answer != number else 'Долго думал'
    print(wrong_message)

    lives -= 1
    if lives < 0:
        print('Game Over')
        break
