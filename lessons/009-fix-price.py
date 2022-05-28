price = 100
print(f'Добро пожаловать в магазин, где всё по {price} рублей')

product = input('Выберите товар: ')
count = int(input('Выберите количество товара: '))

if product == 'хлеб' or product == 'соль':
    # price = price - price * 0.2
    price -= price * 0.2

print(f'С вас {price * count} рублей')
