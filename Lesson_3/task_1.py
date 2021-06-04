"""
Задание 1.
Реализуйте свои пользовательские функции, в которых реализуйте:
a) заполнение списка и словаря,
   сделайте замеры и сделайте выводы, что выполняется быстрее и почему
b) выполните набор операций и со списком, и со словарем,
   сделайте замеры и сделайте выводы, что и где выполняется быстрее и почему
Подсказка: для замеров воспользуйтесь модулем time (см. примеры урока 1)
Примечание: eсли вы уже знаете, что такое декоратор и как его реализовать,
то реализуйте ф-цию-декоратор для подсчета времени работы ваших пользовательских функций
И примените ее к своим функциям!
Прошу вас внимательно читать ТЗ и не забыть выполнить все пункты.
"""
import time


def time_measure(delegate):
    def wrapper(*args):
        start_time = time.time()
        delegate(*args)
        return time.time() - start_time

    return wrapper


@time_measure
def fill_list_at_begin(list_to_fill: [], num_elements: int):
    for i in range(0, num_elements):
        list_to_fill.insert(0, i)


@time_measure
def fill_list_at_end(list_to_fill: [], num_elements: int):
    for i in range(0, num_elements):
        list_to_fill.append(i)


@time_measure
def fill_list_in_mid(list_to_fill: [], num_elements: int):
    for i in range(0, num_elements):
        list_to_fill.insert(int(i / 2), i)


@time_measure
def fill_dict(dict_to_fill: {}, num_elements: int):
    for i in range(0, num_elements):
        dict_to_fill[i] = i


@time_measure
def move_in_dict(dict_to_use: {}, num_elements: int):  # Передвигаем значения в словаре
    limit = len(dict_to_use)
    for i in range(0, num_elements):
        dict_to_use[(i + 1) % limit] = dict_to_use[i]


@time_measure
def del_from_dict(dict_to_use: {}, num_elements: int):
    for i in range(0, num_elements):
        del dict_to_use[i]


@time_measure
def move_in_list(list_to_use: [], num_elements: int):
    limit = len(list_to_use)
    for i in range(0, num_elements):
        list_to_use[(i + 1) % limit] = list_to_use[i]


@time_measure
def del_from_list_begin(list_to_use: [], num_elements: int):
    for i in range(0, num_elements):
        list_to_use.pop(0)


@time_measure
def del_from_list_mid(list_to_use: [], num_elements: int):
    for i in range(0, num_elements):
        list_to_use.pop(int(len(list_to_use) / 2))


@time_measure
def del_from_list_end(list_to_use: [], num_elements: int):
    for i in range(0, num_elements):
        list_to_use.pop()


test_list = []
test_list_2 = []
test_list_3 = []
test_dict = {}

num_of_elements = 200000

# Part 1 - filling data
# Сложность указывается для каждой операции вставки
print(f'Elapsed time - fill_dict: {fill_dict(test_dict, num_of_elements)}')  # O(1)
print(f'Elapsed time - fill_list_at_begin: {fill_list_at_begin(test_list, num_of_elements)}')  # O(n)
print(f'Elapsed time - fill_list_at_end: {fill_list_at_end(test_list_2, num_of_elements)}')  # O(1)
print(f'Elapsed time - fill_list_in_mid: {fill_list_in_mid(test_list_3, num_of_elements)}')  # O(n)

print(f'Size of test_list: {len(test_list)}')
print(f'Size of test_list_2: {len(test_list_2)}')
print(f'Size of test_list_3: {len(test_list_3)}')
print(f'Size of test_dict: {len(test_dict)}')

# Part 2 - operations
print(f'Elapsed time - move_in_dict: {move_in_dict(test_dict, num_of_elements)}')  # O(1)
print(f'Elapsed time - del_from_dict: {del_from_dict(test_dict, num_of_elements)}')  # O(1)
print(f'Elapsed time - move_in_list: {move_in_list(test_list, num_of_elements)}')  # O(1)
print(f'Elapsed time - del_from_list_begin: {del_from_list_begin(test_list, num_of_elements)}')  # O(n)
print(f'Elapsed time - del_from_list_end: {del_from_list_end(test_list_2, num_of_elements)}')  # O(1)
print(f'Elapsed time - del_from_list_mid: {del_from_list_mid(test_list_3, num_of_elements)}')  # O(n)

print(f'Size of test_list: {len(test_list)}')
print(f'Size of test_list_2: {len(test_list_2)}')
print(f'Size of test_list_3: {len(test_list_3)}')
print(f'Size of test_dict: {len(test_dict)}')

# Results:

# Part 1

# Elapsed time - fill_dict: 0.031239748001098633
# Elapsed time - fill_list_at_begin: 7.951256513595581
# Elapsed time - fill_list_at_end: 0.03128361701965332
# Elapsed time - fill_list_in_mid: 3.858431100845337
# Size of test_list: 200000
# Size of test_list_2: 200000
# Size of test_list_3: 200000
# Size of test_dict: 200000

# Наполнение словаря и списка в конец происходит примерно за одинаковое время O(1),
# а списков вставкой в начало и середину - за большее время O(n),
# т.к., добавляя новый элемент, каждый раз приходится сдвигать остальные элементы.


#  Part 2

# Elapsed time - move_in_dict: 0.062485456466674805
# Elapsed time - del_from_dict: 0.015621185302734375
# Elapsed time - move_in_list: 0.06248354911804199
# Elapsed time - del_from_list_begin: 2.2963366508483887
# Elapsed time - del_from_list_end: 0.03124260902404785
# Elapsed time - del_from_list_mid: 1.1247749328613281
# Size of test_list: 0
# Size of test_list_2: 0
# Size of test_list_3: 0
# Size of test_dict: 0

# Перемещение элемента в словаре и списке происходит примерно за одинаковое время O(1),
# удаление элементов из словаря и с конца списка также примерно за одинаковое время O(1),
# а удаление элементов из начала и середины списка - за большее время O(n),
# т.к., удаляя элемент, каждый раз приходится сдвигать остальные элементы.
