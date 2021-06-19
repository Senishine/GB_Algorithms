"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50). Выведите на экран исходный
и отсортированный массивы.
Хотя в примерах к уроку уже есть вариант реализации слияния,
попробуйте предложить другой (придумать или найти).
И попытаться сделать замеры на массивах разной длины: 10, 100, 1000, ...
Пример:
Введите число элементов: 5
Исходный - [46.11436617832828, 41.62921998361278, 18.45859540989644, 12.128870723745806, 8.025098788570562]
Отсортированный - [8.025098788570562, 12.128870723745806, 18.45859540989644, 41.62921998361278, 46.11436617832828]
"""

from random import uniform
from timeit import timeit


def merge_sort(arr):
    if len(arr) < 2:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    i = j = 0
    left_size = len(left)
    right_size = len(right)
    result = []
    while i < left_size and j < right_size:
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    return result + left[i:] + right[j:]


def rand_list(n):
    return [uniform(0, 50) for _ in range(n)]


num_elements = int(input("Input elements count: "))
test_data = rand_list(num_elements)

print(f"Исходный массив: {test_data}")
print(f"Отсортированный массив: {merge_sort(test_data)}")

iterations = 1000
list_10 = rand_list(10)
list_100 = rand_list(100)
list_1000 = rand_list(1000)

print(f"list_10: {timeit(lambda: merge_sort(list_10), number=iterations)}")
print(f"list_100: {timeit(lambda: merge_sort(list_100), number=iterations)}")
print(f"list_1000: {timeit(lambda: merge_sort(list_1000), number=iterations)}")

# Input elements count: 15
# Исходный массив: [17.226153459600873, 49.99467128665835, 37.085926667605115, 10.150797148674862, 20.642217543015512, 16.56115521441831, 49.19118619010453, 29.859303192300008, 39.31811378800242, 48.45762299873203, 17.6076918302487, 30.178455265558647, 42.81573223533142, 24.063763453773067, 16.47551174669862]
# Отсортированный массив: [10.150797148674862, 16.47551174669862, 16.56115521441831, 17.226153459600873, 17.6076918302487, 20.642217543015512, 24.063763453773067, 29.859303192300008, 30.178455265558647, 37.085926667605115, 39.31811378800242, 42.81573223533142, 48.45762299873203, 49.19118619010453, 49.99467128665835]
# list_10: 0.011471499999999857
# list_100: 0.19081409999999988
# list_1000: 2.5776053

# Работает быстрее, чем сортировка пузырьком и другие алгоритмы с квадратичной сложностью особенно при больших N
# Расход памяти O(n) (для сравнения пузырьком O(1))
# Без использования рекурсии алгоритм сильно усложняется
