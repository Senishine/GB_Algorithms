"""
Задание 4.
Приведены два алгоритма. В них определяется число,
которое встречается в массиве чаще всего.
Сделайте профилировку каждого алгоритма через timeit
Попытайтесь написать третью версию, которая будет самой быстрой.
Сделайте замеры и опишите, получилось ли у вас ускорить задачу.
Без аналитики задание считается не принятым!
"""
import random
import timeit

# array = [1, 3, 1, 3, 4, 5, 1, 3]

array = [random.randint(0, 100) for _ in range(100)]


def func_1():
    m = 0
    num = 0
    for i in array:
        count = array.count(i)
        if count > m:
            m = count
            num = i
    return f'Чаще всего встречается число {num}, ' \
           f'оно появилось в массиве {m} раз(а)'


def func_2():
    new_array = []
    for el in array:
        count2 = array.count(el)
        new_array.append(count2)

    max_2 = max(new_array)
    elem = array[new_array.index(max_2)]
    return f'Чаще всего встречается число {elem}, ' \
           f'оно появилось в массиве {max_2} раз(а)'


def func_3():
    numbers_count = {}
    for el in array:
        value = numbers_count.get(el)
        if value is None:
            value = 0
        value += 1
        numbers_count[el] = value
    max_value = max(numbers_count.values())  # maximum value
    max_keys = [k for k, v in numbers_count.items() if v == max_value]  # getting all keys containing the `maximum`
    return f"The most frequent numbers is [numbers={max_keys}, count={max_value}]"


def func_4():
    numb = max(array, key=array.count)
    return f"The most frequent numbers is [numbers={array.count(numb)}, count={numb}]"


print(func_1())
print(func_2())
print(func_3())
print(func_4())

print(f"func_1 time is: {timeit.timeit(lambda: func_1(), number=10000)}")
print(f"func_2 time is: {timeit.timeit(lambda: func_2(), number=10000)}")
print(f"func_3 time is: {timeit.timeit(lambda: func_3(), number=10000)}")
print(f"func_4 time is: {timeit.timeit(lambda: func_4(), number=10000)}")

# list size - 100
# func_1 time is: 3.171644
# func_2 time is: 3.2605225
# func_3 time is: 0.35447589999999973
# func_4 time is: 3.0609957000000003

# В общем случае  алгоритм построенный на базе словаря выполняется быстрее т.к. имеет меньшую сложность O(1)
# в сравнении с первыми двумя ф-циями O(n)
# При небольшом размере списка первые два алгоритма могут работать также или быстрее т.к. обход небольшого списка
# сопоставим по сложности с вычислением хеш ф-ции для ключей в словаре
# Однако уже для размера в 100 элементов алгоритм построенный на базе словаря выполняется значительно быстрее,
# чем на полном обходе списка
