"""
Задание 2.*
Предложить еще какие-либо варианты (механизмы, подходы, библиотеки, идеи)
для оптимизации памяти и
доказать!!! (наглядно, кодом) их эффективность (на примере профилировщика).
"""

import timeit
import memory_profiler


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


def get_even_numbers_iter(n):
    for i in range(n):
        if i % 2 == 0:
            yield i


def get_even_numbers_list(n):
    return [i for i in range(n) if i % 2 == 0]


@profiler
def sum_of(func):
    total = 0
    for i in range(10):
        total += sum(func())
    return total


size = 10000000
assert list(get_even_numbers_iter(size)) == get_even_numbers_list(size)

print(f"get_even_numbers_iter: {sum_of(lambda: get_even_numbers_iter(size))}")
print(f"get_even_numbers_list: {sum_of(lambda: get_even_numbers_list(size))}")

# get_even_numbers_iter: (0.0078125, 1.0690532999999998)
# get_even_numbers_list: (1.5, 1.1234230000000003)
# Видно, что в случае использования итераторов не используется дополительная память для промежуточного списка
# Как следствие расход памяти для подсчета суммы в этом сучае значительно ниже, чем в случае с созданием списка
