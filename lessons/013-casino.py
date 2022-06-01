from random import randint

print('Добро пожаловать в казино "Проигранная корова"')
print('----------------------------------------------')
money = int(input('Сделайте свою ставку: '))

guess_min = 1
guess_max = 5
num = randint(guess_min, guess_max)

if int(input(f'Угадай число от {guess_min} до {guess_max}: ')) == num:
    print('Ура! Ты победил с первого раза!')
    print(f'Казино удваивает твою сумму {money * 2}')
else:
    if int(input('Давай ещё раз: ')) == num:
        print('Неплохо! Ты всё-равно в выиграше!')
        print(f'Казино дарит тебе половину твоей суммы {money * 1.5}')
    else:
        if int(input('Ну всё, последний шанс: ')) == num:
            print(f'На {money}, забирай свои деньги и иди домой!')
        else:
            print('Увы, но вы остаётесь ни с чем!')
