"""
Задача 3.
В соответствии с документацией Python,
deque – это обобщение стеков и очередей.
Вот основное правило: если вам нужно что-то быстро дописать или вытащить, используйте deque.
Если вам нужен быстрый случайный доступ, используйте list.
Задача:
1) создайте простой список (list) и очередь (deque). Сделайте замеры и оцените что заполняется быстрее.
2) Выполните различные операции с каждым из объектов. Сделайте замеры и оцените, где и какие операции быстрее.
Не забудьте, что сравнивать, например, можно операцию appendleft дека и insert списка и т.д.
"""

from collections import deque
import timeit


def fill_list_at_end(n) -> list:
    test_list = []
    for i in range(0, n):
        test_list.append(i)
    return test_list


def fill_deque_at_end(n) -> deque:
    test_deque = deque()
    for i in range(0, n):
        test_deque.append(i)
    return test_deque


def fill_list_at_begin(n) -> list:
    test_list = []
    for i in range(0, n):
        test_list.insert(0, i)
    return test_list


def fill_deque_at_begin(n) -> deque:
    test_deque = deque()
    for i in range(0, n):
        test_deque.appendleft(i)
    return test_deque


iterations = 10000
size = 1000
my_deque = fill_deque_at_end(size)
my_list = fill_list_at_end(size)

print(f"filling list at the begin: {timeit.timeit(lambda: fill_list_at_begin(size), number=iterations)}")
print(f"filling deque at the begin: {timeit.timeit(lambda: fill_deque_at_begin(size), number=iterations)}")

print(f"filling list at the end: {timeit.timeit(lambda: fill_list_at_end(size), number=iterations)}")
print(f"filling deque at the end: {timeit.timeit(lambda: fill_deque_at_end(size), number=iterations)}")

# iterate over collections using 'sum' function
print(f"iterating through list: {timeit.timeit(lambda: sum(my_list), number=iterations)}")
print(f"iterating through deque: {timeit.timeit(lambda: sum(my_deque), number=iterations)}")

# iterate over collections using 'reverse' function
print(f"iterating through list - reverse: {timeit.timeit(lambda: my_list.reverse(), number=iterations)}")
print(f"iterating through deque - reverse: {timeit.timeit(lambda: my_deque.reverse(), number=iterations)}")

# filling list at the begin: 3.1125429000000002
# filling deque at the begin: 0.8511633000000001
# filling list at the end: 0.8796451999999997
# filling deque at the end: 0.8579191999999995
# iterating through list: 0.09613700000000058
# iterating through deque: 0.11168000000000067
# iterating through list - reverse: 0.00637880000000024
# iterating through deque - reverse: 0.018147500000000427

# В случае вставки элемента в начало (слева) deque выигрывает в скорости,
# т.к. не требуется смещения всех элементов правее на одну позицию,
# соответственно, сложность вставки deque O(1) против O(n) в списке.
# В случае вставки в конец коллекции (справа) время примерно одинаковое,
# т.к. ни в одной, ни в другой коллекции не требуется никаких дополнительный действий.
# Перебор элементов происходит незначительно быстрее в списке, вероятнее всего из-за того,
# что данная коллекция более оптимально расположена в памяти (не ссылочная структура - массив),
# все элементы расположены рядом.
