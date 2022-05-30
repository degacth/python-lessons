from getpass import getpass


login = input('Введите логин: ')
password = getpass('Введите пароль: ')

if login == 'admin' and password == '12345':
    print(f'Добро пожаловать {login}')
else:
    print('Неверные данные аутентификации')
