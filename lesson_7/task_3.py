"""
3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на
две равные по длине части: в одной находятся элементы, которые не меньше медианы,
в другой – не больше медианы.
Задачу можно решить без сортировки исходного массива.
Но если это слишком сложно, то используйте метод сортировки,
который не рассматривался на уроках: Шелла, Гномья, Кучей...
[5, 3, 4, 3, 3, 3, 3]
[3, 3, 3, 3, 3, 4, 5]
my_lst
new_lts
arr[m]
from statistics import median
[3, 4, 3, 3, 5, 3, 3]
left = []
right = []
left == right and
for i in
    for
    left == right
    left.clear()
    right.clear()
"""

import heapq
from random import randint
from statistics import median
from timeit import timeit


def median_sort(data):
    data.sort()
    return data[len(data) // 2]


def heap_sort(source):
    def leaf_search(data, start, end):
        current = start
        while True:
            child = current * 2 + 1
            if child + 1 > end:
                break
            if data[child + 1] > data[child]:
                current = child + 1
            else:
                current = child
        child = current * 2 + 1
        if child <= end:
            current = child
        return current

    def sift_up(data, start, end):
        current = leaf_search(data, start, end)
        while data[start] > data[current]:
            current = (current - 1) // 2
        temp = data[current]
        data[current] = data[start]

        while current > start:
            current = (current - 1) // 2
            temp, data[current] = data[current], temp

    size = len(source) - 1
    for i in range((len(source) - 2) // 2, -1, -1):
        sift_up(source, i, size)

    for i in range(size, 0, -1):
        source[i], source[0] = source[0], source[i]
        sift_up(source, 0, i - 1)
    return source


def median_heap_sort(data):
    heap_sort(data)
    return data[len(data) // 2]


def median_max_remove(data):
    median_value = data[0]
    for i in range(0, len(data) // 2 + 1):
        median_value = max(data)
        data.remove(median_value)
    return median_value


def median_heapify(data):
    return heapq.nlargest(len(data) // 2 + 1, data).pop()


iterations = 100
seq_size = int(input('Input sequence size: '))
test_list = [randint(1, 10000) for i in range(2 * seq_size + 1)]
print(f"{test_list}")
print(f"{median(test_list.copy())}")
print(f"{median_sort(test_list.copy())}")
print(f"{median_heap_sort(test_list.copy())}")
print(f"{median_max_remove(test_list.copy())}")
print(f"{median_heapify(test_list.copy())}")

assert median(test_list.copy()) == median_sort(test_list.copy()) \
       == median_heap_sort(test_list.copy()) == median_max_remove(test_list.copy()) \
       == median_heapify(test_list.copy())

print(f"median: {timeit(lambda: median(test_list.copy()), number=iterations)}")
print(f"median_sort: {timeit(lambda: median_sort(test_list.copy()), number=iterations)}")
print(f"median_heap_sort: {timeit(lambda: median_heap_sort(test_list.copy()), number=iterations)}")
print(f"median_max_remove: {timeit(lambda: median_max_remove(test_list.copy()), number=iterations)}")
print(f"median_heapify: {timeit(lambda: median_heapify(test_list.copy()), number=iterations)}")

# Input sequence size: 1000

# 5030
# 5030
# 5030
# 5030
# 5030
# median: 0.026105000000000267
# median_sort: 0.02400570000000002
# median_heap_sort: 0.7585677
# median_max_remove: 3.1613811999999997
# median_heapify: 0.09344470000000005
