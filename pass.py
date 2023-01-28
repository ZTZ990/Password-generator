from random import *

def yn_check(check):
    if check.lower() in 'yn':
        return True
    else:
        return False

def generate_password(alpha,length):
    password = ''
    for i in range(length):
        password += choice(alpha)
    return password

digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
exceptions = 'il1Lo0O'

chars = ''

password_amount = int(input('Укажите количество паролей для генерации: '))
password_lenght = int(input('Введите длину одного пароля: '))

dig_on = input(f'Включать цифры {digits} ? (y/n) ')
while yn_check(dig_on) == False:
    dig_on = input(f'Неверный ввод. Включать цифры {digits} ? (y/n) ')

abc_on = input(f'Включать нижний регистр {lowercase_letters} ? (y/n) ')
while yn_check(abc_on) == False:
    abc_on = input(f'Неверный ввод. Включать нижний регистр {lowercase_letters} ? (y/n) ')

ABC_on = input(f'Включать верхний регистр {uppercase_letters} ? (y/n) ')
while yn_check(ABC_on) == False:
    ABC_on = input(f'Неверный ввод. Включать верхний регистр {uppercase_letters} ? (y/n) ')

pun_on = input(f'Включить знаки{punctuation} ? (y/n) ')
while yn_check(pun_on) == False:
    pun_on = input(f'Неверный ввод. Включить знаки{punctuation} ? (y/n) ')

exc_on = input(f'Исключить {exceptions} ? (y/n) ')
while yn_check(exc_on) == False:
    exc_on = input(f'Неверный ввод. Исключить {exceptions} ? (y/n) ')

if dig_on == 'y':
    chars += digits
if abc_on == 'y':
    chars += lowercase_letters
if ABC_on == 'y':
    chars += uppercase_letters
if pun_on == 'y':
    chars += punctuation 
if exc_on == 'y':
    for i in range(0,len(exceptions)):
        chars = chars.replace(exceptions[i],'')

if chars == '':
    print('Не выбран ни один набор символов.')
else:
    for i in range(password_amount):
        print(generate_password(chars,password_lenght))
        

    

