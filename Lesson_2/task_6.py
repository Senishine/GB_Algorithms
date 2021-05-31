"""
6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.
Подсказка:
Базовый случай здесь - угадали число или закончились попытки
Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
"""

from random import randint


def get_number():
    try:
        number = int(input('input number from 0 to 100: '))
        return number
    except ValueError:
        print(f'Incorrect number')
        return get_number()


def riddle(attempts=10):
    secret_num = randint(0, 100)
    guess_number(secret_num, 0, attempts)


def guess_number(secret_num, current_attempt, limit):
    user_number = get_number()
    if user_number == secret_num:
        print(f'You won [secret number={secret_num}]')
        return
    if current_attempt + 1 == limit:
        print(f'You lost [secret number={secret_num}]')
    if user_number < secret_num:
        print('Secret number is grater than yours')
    else:
        print('Secret number is smaller than yours')
    guess_number(secret_num, current_attempt+1, limit)


riddle()
