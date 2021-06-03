"""
7.	Напишите программу, доказывающую или проверяющую, что для множества
натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
где n - любое натуральное число.
Рекурсия вам нужна для решения левой части выражения.
Полученный результат нужно просто сравнить с результатом в правой.
Пример:
для n = 5
1+2+3+4+5 = 5(5+1)/2
Подсказка:
Правой части в рекурсии быть не должно. Необходимо сравнить результат, который даст рекурсивная ф-ция
со значением, полученным в правой части (здесь нужно просто подставить n и подсчитать)
Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
"""


def read_number():
    try:
        number = int(input('input number: '))
        return number
    except ValueError:
        print(f'Incorrect number')
        read_number()


def sum_of_sequence(size):
    return add_next_number(1, size), int(size * (size + 1) / 2)


def add_next_number(current_number, limit):
    return current_number + (add_next_number(current_number + 1, limit) if current_number < limit else 0)


n = read_number()
result = sum_of_sequence(n)
print(result)
assert result[0] == result[1]
