"""
Задание 1.
Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива
Сделайте замеры времени выполнения кода с помощью модуля timeit
Оптимизируйте, чтобы снизить время выполнения
Проведите повторные замеры.
Добавьте аналитику: что вы сделали и почему!!!
Без аналитики задание не принимается
"""

import timeit
import random
import dis


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


def func_2(nums):
    new_arr = []
    for idx, val in enumerate(nums):
        if val % 2 == 0:
            new_arr.append(idx)
    return new_arr


def func_3(nums):
    return [idx for idx, val in enumerate(nums) if val % 2 == 0]


def func_4_lazy(nums):
    return map(lambda value: value[0], filter(lambda value: value[1] % 2 == 0, enumerate(nums)))


def func_5_lazy(nums):
    return (idx for idx, val in enumerate(nums) if val % 2 == 0)


list_size = 200
iterations = 100000
nums_list = [random.randint(0, 10000) for n in range(list_size)]

assert func_1(nums_list) == func_2(nums_list) == func_3(nums_list) == list(func_4_lazy(nums_list)) == list(
    func_5_lazy(nums_list))

print(f"func_1: {timeit.timeit(lambda: func_1(nums_list), number=iterations)}")
print(f"func_2: {timeit.timeit(lambda: func_2(nums_list), number=iterations)}")
print(f"func_3: {timeit.timeit(lambda: func_3(nums_list), number=iterations)}")
print(f"func_4_lazy: {timeit.timeit(lambda: func_4_lazy(nums_list), number=iterations)}")
print(f"func_5_lazy: {timeit.timeit(lambda: func_5_lazy(nums_list), number=iterations)}")

# func_1: 1.9300689
# func_2: 1.9616647
# func_3: 1.5989121000000002
# func_4_lazy: 0.06096630000000047
# func_5_lazy: 0.058080200000000026


# Ф-ции не создающие списки отрабатывают значительо быстрее, так что если есть возможность,
# лучше использовать ленивую инициализацию (итераторы) в этом случае можно избежать лишней работы (цикла)
# В случае если все же нужен именно список то ф-ция использующая list comprehension
# работает быстрее чем вариант с циклом это объясняется тем, что в этом случае используется специальная команда
# LIST_APPEND https://docs.python.org/3/library/dis.html#opcode-LIST_APPEND вместо обычного вызова list.append
# который осуществляется 4-мя командами. Следовательно суммарное количество операций уменьшается и
# соответственно уменьшается время выполнения


dis.dis(func_1)
# 18           0 BUILD_LIST               0
#              2 STORE_FAST               1 (new_arr)
#
# 19           4 LOAD_GLOBAL              0 (range)
#              6 LOAD_GLOBAL              1 (len)
#              8 LOAD_FAST                0 (nums)
#             10 CALL_FUNCTION            1
#             12 CALL_FUNCTION            1
#             14 GET_ITER
#        >>   16 FOR_ITER                30 (to 48)
#             18 STORE_FAST               2 (i)
#
# 20          20 LOAD_FAST                0 (nums)
#             22 LOAD_FAST                2 (i)
#             24 BINARY_SUBSCR
#             26 LOAD_CONST               1 (2)
#             28 BINARY_MODULO
#             30 LOAD_CONST               2 (0)
#             32 COMPARE_OP               2 (==)
#             34 POP_JUMP_IF_FALSE       16
#
# 21          36 LOAD_FAST                1 (new_arr)
#             38 LOAD_METHOD              2 (append)
#             40 LOAD_FAST                2 (i)
#             42 CALL_METHOD              1
#             44 POP_TOP
#             46 JUMP_ABSOLUTE           16
# 22     >>   48 LOAD_FAST                1 (new_arr)
#             50 RETURN_VALUE

dis.dis(func_2)
# 26            0 BUILD_LIST               0
#               2 STORE_FAST               1 (new_arr)
#
#  27           4 LOAD_GLOBAL              0 (enumerate)
#               6 LOAD_FAST                0 (nums)
#               8 CALL_FUNCTION            1
#              10 GET_ITER
#         >>   12 FOR_ITER                30 (to 44)
#              14 UNPACK_SEQUENCE          2
#              16 STORE_FAST               2 (idx)
#              18 STORE_FAST               3 (val)
#
#  28          20 LOAD_FAST                3 (val)
#              22 LOAD_CONST               1 (2)
#              24 BINARY_MODULO
#              26 LOAD_CONST               2 (0)
#              28 COMPARE_OP               2 (==)
#              30 POP_JUMP_IF_FALSE       12
#
#  29          32 LOAD_FAST                1 (new_arr)
#              34 LOAD_METHOD              1 (append)
#              36 LOAD_FAST                2 (idx)
#              38 CALL_METHOD              1
#              40 POP_TOP
#              42 JUMP_ABSOLUTE           12
#
#  30     >>   44 LOAD_FAST                1 (new_arr)
#              46 RETURN_VALUE


dis.dis(func_3)
# 34            0 BUILD_LIST               0
#               2 LOAD_FAST                0 (.0)
#         >>    4 FOR_ITER                24 (to 30)
#               6 UNPACK_SEQUENCE          2
#               8 STORE_FAST               1 (idx)
#              10 STORE_FAST               2 (val)
#              12 LOAD_FAST                2 (val)
#              14 LOAD_CONST               0 (2)
#              16 BINARY_MODULO
#              18 LOAD_CONST               1 (0)
#              20 COMPARE_OP               2 (==)
#              22 POP_JUMP_IF_FALSE        4
#              24 LOAD_FAST                1 (idx)
#              26 LIST_APPEND              2
#              28 JUMP_ABSOLUTE            4
#         >>   30 RETURN_VALUE
