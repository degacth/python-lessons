print('Добро пожаловать в зоопарк домашних животных')
pet = input('Введите животное которое хотите видеть: ')

cat = u'\U0001F431'
dog = u'\U0001F436'
cow = u'\U0001F42E'
# мышь 1F42D

if pet == 'кот':
    print(cat)
elif pet == 'собака':
    print(dog)
elif pet == 'корова':
    print(cow)
else:
    print(f'У нас нет такого животного: {pet}')
