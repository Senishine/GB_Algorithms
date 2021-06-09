"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните операции с каждым их них (заполнение, получение элемента) и сделайте замеры.
Опишите полученные результаты, сделайте выводы.
И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях?
"""
from collections import OrderedDict
import timeit


def fill_dict(n):
    my_dict = {}
    for i in range(n):
        my_dict[i] = i
    return my_dict


def fill_ordered_dict(n):
    my_dict = OrderedDict()
    for i in range(n):
        my_dict[i] = i
    return my_dict


def get_dict(n, dict_obj):
    for i in range(n):
        dict_obj[i + 1] = dict_obj[i]


size = 1000
iterations = 10000
test_dict = fill_dict(size)
test_ordered_dict = fill_ordered_dict(size)

print(f"fill_dict: {timeit.timeit(lambda: fill_dict(size), number=iterations)}")
print(f"fill_ordered_dict: {timeit.timeit(lambda: fill_ordered_dict(size), number=iterations)}")
print(f"get_dict: {timeit.timeit(lambda: get_dict(size, test_dict), number=iterations)}")
print(f"get_dict (ordered): {timeit.timeit(lambda: get_dict(size, test_ordered_dict), number=iterations)}")

# fill_dict: 0.7294164000000001
# fill_ordered_dict: 1.2549648999999998
# get_dict: 1.2864225
# get_dict (ordered): 1.6079600999999997

# OrderedDict работает медленнее, чем стандартный словарь, и, т.к. страндартный словарь с версии 3.6
# сохраняет порядок вставки элементов, то использовать OrderedDict с этой версии Python не имеет смысла