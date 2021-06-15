"""
Задание 3 *.
Сделать профилировку для скриптов с рекурсией и сделать описание,
можно ли так профилировать и есть ли 'подводные камни' в профилировании?
Придумать как это решить!
Есть очень простое решение
"""

from memory_profiler import profile


def recursive_reverse(number):
    if number == 0:
        return ''
    return f'{str(number % 10)}{recursive_reverse(number // 10)}'


@profile
def reverse(number):
    return recursive_reverse(number)


print(reverse(1234567891234598765432142))

# Профилировка рекурсивных ф-ций нежелательна, так как теряется связь между входными параметрами и
# результатами профилирования из-за того, что профилирование выполняется для каждого вызова ф-ции.
# Поэтому лучше обернуть ф-цию в отдельную нерекурсивную и профилировать её
# Line #    Mem usage    Increment  Occurences   Line Contents
# ============================================================
#     18     18.5 MiB     18.5 MiB           1   @profile
#     19                                         def reverse(number):
#     20     18.5 MiB      0.0 MiB           1       return recursive_reverse(number)
#
#
# 2412345678954321987654321
