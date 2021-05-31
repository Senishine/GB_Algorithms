"""
4.	Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.
Пример:
Введите количество элементов: 3
Количество элементов: 3, их сумма: 0.75
Подсказка:
Каждый очередной элемент в 2 раза меньше предыдущего и имеет противоположный знак
Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
"""


def __next_sequence_item__(element, current_index, limit):
    if current_index == limit:
        return 0
    current_element = -element / 2
    return current_element + __next_sequence_item__(current_element, current_index + 1, limit)


def sequence_sum(limit):
    if limit < 1:
        raise ValueError(f'Limit must be grater than zero [actual={limit}]')
    return 1 + __next_sequence_item__(1, 1, limit)


def read_number(message):
    source = ''
    try:
        source = input(message)
        elements_count = int(source)
        if elements_count < 0:
            print(f'Negative number {elements_count}')
            return read_number(message)
        return elements_count
    except ValueError:
        print(f'Incorrect number {source}, try again please')
        return read_number(message)


print(sequence_sum(read_number("Input sequence size: ")))
