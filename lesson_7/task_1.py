"""
1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран
исходный и отсортированный массивы.
Сортировка должна быть реализована в виде функции.
Обязательно доработайте алгоритм (сделайте его умнее).
Идея доработки: если за проход по списку не совершается ни одной сортировки,
то завершение. Обязательно сделайте замеры времени обеих реализаций
и обосновать дала ли оптимизация эффективность
Подсказка: обратите внимание, сортируем не по возрастанию, как в примере,
а по убыванию.
Сделайте выводы!!!
Опишите в чем была ваша доработка и помогла ли вам доработка??
"""

import random
import timeit


def bubble_sort_1(source):
    if source is None:
        return
    size = len(source)
    if size < 2:
        return
    for i in range(size - 1):
        for j in range(size - 1):
            if source[j] < source[j + 1]:
                source[j], source[j + 1] = source[j + 1], source[j]


def bubble_sort_2(source):
    if source is None:
        return
    size = len(source)
    if size < 2:
        return
    for i in range(size - 1):
        for j in range(size - i - 1):
            if source[j] < source[j + 1]:
                source[j], source[j + 1] = source[j + 1], source[j]


def bubble_sort_3(source):
    if source is None:
        return
    size = len(source)
    if size < 2:
        return
    for i in range(size - 1):
        swapped = False
        for j in range(size - i - 1):
            if source[j] < source[j + 1]:
                source[j], source[j + 1] = source[j + 1], source[j]
                swapped = True
        if not swapped:
            break


def test_run(test_name, f):
    test_1 = [random.randint(0, 100) for _ in range(0, 100)]
    test_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(f"Before sort {test_name}: {test_1}")
    print(f"Before sort {test_name}: {test_2}")
    f(test_1)
    f(test_2)
    print(f"After sort {test_name}: {test_1}")
    print(f"After sort {test_name}: {test_2}")
    prev = test_1[0]
    for i in test_1:
        assert i <= prev
        prev = i
    prev = test_2[0]
    for i in test_2:
        assert i <= prev
        prev = i


test_run('bubble_sort_1', bubble_sort_1)
test_run('bubble_sort_2', bubble_sort_2)
test_run('bubble_sort_3', bubble_sort_3)

iterations = 100
data_size = 1000

test_list = [random.randint(0, data_size) for _ in range(0, data_size)]

print(f"{timeit.timeit(lambda: bubble_sort_1(test_list.copy()), number=iterations)}")
print(f"{timeit.timeit(lambda: bubble_sort_2(test_list.copy()), number=iterations)}")
print(f"{timeit.timeit(lambda: bubble_sort_3(test_list.copy()), number=iterations)}")

# 13.8345325
# 8.9368731
# 9.3042166

test_list.sort(reverse=True)
print(f"{timeit.timeit(lambda: bubble_sort_1(test_list.copy()), number=iterations)}")
print(f"{timeit.timeit(lambda: bubble_sort_2(test_list.copy()), number=iterations)}")
print(f"{timeit.timeit(lambda: bubble_sort_3(test_list.copy()), number=iterations)}")

# 9.646805800000003
# 5.466580300000004
# 0.009378099999999279

# Оптимизация с неполным проходом внутреннего цикла значительно ускоряет алгоритм при равномерно распределенных
# элеметах т.к. не требуется перебирать уже отсортированную часть массива
# Оптимизация с break помогает для уже упорядоченных (частично упорядоченных) списков, а
# для списков со случайно распределенными элементами результат по времени выполнения примерно одинаковый
