"""
Задание 1.
Выполните профилирование памяти в скриптах
Проанализировать результат и определить программы с
наиболее эффективным использованием памяти.
Примечание: Для анализа возьмите любые 3-5 ваших РАЗНЫХ скриптов!
(хотя бы 3 разных для получения оценки отл).
На каждый скрипт вы должны сделать как минимум по две реализации.
Можно взять только домашние задания с курса Основ
или с текущего курса Алгоритмов
Результаты профилирования добавьте в виде комментариев к коду.
Обязательно сделайте аналитику (что с памятью в ваших скриптах, в чем ваша оптимизация и т.д.)
ВНИМАНИЕ: ЗАДАНИЯ, В КОТОРЫХ БУДУТ ГОЛЫЕ ЦИФРЫ ЗАМЕРОВ (БЕЗ АНАЛИТИКИ)
БУДУТ ПРИНИМАТЬСЯ С ОЦЕНКОЙ УДОВЛЕТВОРИТЕЛЬНО
Попытайтесь дополнительно свой декоратор используя ф-цию memory_usage из memory_profiler
С одновременным замером времени (timeit.default_timer())!
"""

import memory_profiler
import timeit
from numpy import array
from random import randint
from pympler import asizeof
from collections import deque, OrderedDict, namedtuple

# Script 1

test_list_comp = [randint(0, 1000) for el in range(10000)]
test_array = array(test_list_comp)
test_list = []
for el in test_list_comp:
    test_list.append(el)
test_array_1 = array(test_list)
test_list_from_list = list(test_list)

print(f"list comprehension: {asizeof.asizeof(test_list_comp)}")
print(f"array from list comprehension: {asizeof.asizeof(test_array)}")
print(f"regular list: {asizeof.asizeof(test_list)}")
print(f"array from list: {asizeof.asizeof(test_array_1)}")
print(f"list from list: {asizeof.asizeof(test_list_from_list)}")


# array снижает количество потребляемой памяти тк внутри использует не ссылочные структуры, а располагает значения рядом
# то есть массив по структуре становится похожим на массив в языках С и С++
# платой за это становится то, что в массиве можно хранить элементы только одного типа
# Код ниже приведет к ошибке, т.к. в массиве уже находятся int
#     test_array[4] = "qwerty"
# ValueError: invalid literal for int() with base 10: 'qwerty'
# Также видно, что создание списка из уже имеющегося списка расходует меньше памяти
# вероятно это связано с тем что при вызове ф-ции list заранее известна длина будущего списка
# и это значит что можно выделить ровно столько памяти сколько требуется чтобы сохранить все элементы списка, который
# передан в качестве аргумента. Напротив при добавлении поэлементно и при создании через генератор длина заранее
# неизвестна, и поэтому длина внутреннего массива увеличивается с запасом по мере роста списка (удваивается)
# то есть в любой момент времени могут быть выделенны незаполненные элементы внутреннего массива
# этим можно объяснить разницу в памяти между regular list: 333432 и list from list: 326832
# 333432 - 326832 = память еще незаполненных, но уже выделенных ячеек
# ---------------------
# list comprehension: 333432
# array from list comprehension: 40120
# regular list: 333432
# array from list: 40120
# list from list: 326832


# Script 2

class HexNumberDyn:
    def __init__(self, hex_str):
        self.hex_list = [char for char in hex_str]
        self.num = int(hex_str, 16)

    def __add__(self, hex_num):
        hex_sum = self.num + hex_num.num
        return HexNumberDyn(format(hex_sum, 'x'))

    def __mul__(self, hex_num):
        hex_sum = self.num * hex_num.num
        return HexNumberDyn(format(hex_sum, 'x'))

    def __str__(self):
        return hex(self.num)

    def as_list(self):
        return self.hex_list


class HexNumberSlots:
    __slots__ = ['hex_list', 'num']

    def __init__(self, hex_str):
        self.hex_list = [char for char in hex_str]
        self.num = int(hex_str, 16)

    def __add__(self, hex_num):
        hex_sum = self.num + hex_num.num
        return HexNumberDyn(format(hex_sum, 'x'))

    def __mul__(self, hex_num):
        hex_sum = self.num * hex_num.num
        return HexNumberDyn(format(hex_sum, 'x'))

    def __str__(self):
        return hex(self.num)

    def as_list(self):
        return self.hex_list


HexNumberTuple = namedtuple('HexNumberTuple', ['hex_list', 'num'])

dyn = HexNumberDyn("abcdef")
slots = HexNumberSlots("abcdef")
tuple_hex = HexNumberTuple([char for char in "abcdef"], int("abcdef", 16))
print(f"dyn: {asizeof.asizeof(dyn)}")
print(f"slots: {asizeof.asizeof(slots)}")
print(f"tuple: {asizeof.asizeof(tuple_hex)}")


# При использовании slots не создается словарь аттрибутов __dict__,
# что уменьшает объем памяти выделяемый на содание экземпляра на 25-30%
# Однако данный подход ограничивает в создании динамических аттрибутов,
# а также может стать проблемой при множественном наследовании
# namedtuple чуть больше потребляет памяти, чем объект со slots т.к. имеет еще индексированный доступ к полям
# например tuple_hex[0]
# --------------------
# dyn: 760
# slots: 536
# tuple: 544


# Script 3

def profiler(func):
    def wrapper(*args):
        m1 = memory_profiler.memory_usage()
        start_time = timeit.default_timer()
        result = func(*args)
        m2 = memory_profiler.memory_usage()
        mem_diff = m2[0] - m1[0]
        time_diff = timeit.default_timer() - start_time
        # Required to calculate memory otherwise result is freed and memory usage does not calculate it
        result = None
        return mem_diff, time_diff

    return wrapper


@profiler
def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


@profiler
def func_2(nums):
    new_arr = []
    for idx, val in enumerate(nums):
        if val % 2 == 0:
            new_arr.append(idx)
    return new_arr


@profiler
def func_3(nums):
    return [idx for idx, val in enumerate(nums) if val % 2 == 0]


@profiler
def func_4_lazy(nums):
    return map(lambda value: value[0], filter(lambda value: value[1] % 2 == 0, enumerate(nums)))


@profiler
def func_5_lazy(nums):
    return (idx for idx, val in enumerate(nums) if val % 2 == 0)


@profiler
def func_deque(nums):
    new_arr = deque()
    for idx, val in enumerate(nums):
        if val % 2 == 0:
            new_arr.append(idx)
    return new_arr


@profiler
def func_set(nums):
    new_arr = set()
    for idx, val in enumerate(nums):
        if val % 2 == 0:
            new_arr.add(idx)
    return new_arr


nums_list = [n for n in range(1000000)]
print(f"func_1: {func_1(nums_list)}")
print(f"func_2: {func_2(nums_list)}")
print(f"func_3: {func_3(nums_list)}")
print(f"func_4_lazy: {func_4_lazy(nums_list)}")
print(f"func_5_lazy: {func_5_lazy(nums_list)}")
print(f"func_deque: {func_deque(nums_list)}")
print(f"func_set: {func_set(nums_list)}")


# Ф-ции не создающие списки отрабатывают значительо быстрее, и расходуют меньше памяти
# т.к. не требуется создавать коллекцию, так что если есть возможность,
# лучше использовать ленивую инициализацию (итераторы) в этом случае можно избежать лишней работы (цикла)
# В случае если все же нужен именно список то ф-ция использующая list comprehension работает быстрее чем вариант с
# циклом, по памяти расход примерно одинаковый
# Deque расходует чуть больше памяти чем список из-за ссылочной организации данных внутри
# Set расходует почти в два раза больше памяти т.к. необходимо хранить и ключи и значения
# func_1: (18.453125, 0.2214509)
# func_2: (19.96875, 0.23779709999999998)
# func_3: (18.1640625, 0.2220435999999999)
# func_4_lazy: (0.0, 0.10895390000000016)
# func_5_lazy: (0.0, 0.10797889999999999)
# func_deque: (18.921875, 0.22016619999999998)
# func_set: (31.19140625, 0.25014670000000017)


# Script 4

@profiler
def fill_dict(n):
    my_dict = {}
    for i in range(n):
        my_dict[i] = i
    return my_dict


@profiler
def fill_ordered_dict(n):
    my_dict = OrderedDict()
    for i in range(n):
        my_dict[i] = i
    return my_dict


print(f"dict: {fill_dict(100000)}")
print(f"ordered dict: {fill_ordered_dict(100000)}")

# Время заполнения dict и OrderedDict примерно одинаковое но dict намного
# эффективнее располагается в памяти благодаря алгоритму сжатия
# https://mail.python.org/pipermail/python-dev/2012-December/123028.html
# dict: (7.76171875, 0.14029789999999975)
# ordered dict: (12.8828125, 0.12446160000000006)
