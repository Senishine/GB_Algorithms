"""
Задание 3.
Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.
Сделайте профилировку каждого алгоритма через cProfile и через timeit
Обязательно предложите еще свой вариант решения и также запрофилируйте!
Сделайте вывод, какая из четырех реализаций эффективнее и почему!!!
Без аналитики задание считается не принятым
"""
from timeit import timeit
from cProfile import run
import dis


def revers_1(enter_num, revers_num=0):
    if enter_num == 0:
        return revers_num
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        return revers_1(enter_num, revers_num)


def revers_2(enter_num, revers_num=0):
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return revers_num


def revers_3(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num


def revers_4(enter_num):
    zero_code = ord('0')

    def __next_item__(num):
        while num != 0:
            next_item = num % 10
            num //= 10
            yield next_item

    return ''.join([chr(val + zero_code) for val in __next_item__(enter_num)])


def revers_5(enter_num):
    return int("".join(reversed(str(enter_num))))


def revers_6(enter_num):
    zero_code = ord('0')
    mul = 1
    result = 0
    for s in str(enter_num):
        result += (ord(s) - zero_code) * mul
        mul *= 10
    return result


num = 10000000000000000

print(f'revers_1: {timeit("revers_1(num)", number=100000, globals=globals())}')
print(f'revers_2: {timeit("revers_2(num)", number=100000, globals=globals())}')
print(f'revers_3: {timeit("revers_3(num)", number=100000, globals=globals())}')
print(f'revers_4: {timeit("revers_4(num)", number=100000, globals=globals())}')
print(f'revers_5: {timeit("revers_5(num)", number=100000, globals=globals())}')
print(f'revers_6: {timeit("revers_6(num)", number=100000, globals=globals())}')

# revers_1: 0.9489956
# revers_2: 0.6151733
# revers_3: 0.08054439999999996
# revers_4: 0.9424075000000001
# revers_5: 0.2241219000000001
# revers_6: 0.520518

run('revers_1(num)')
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#   18/1    0.000    0.000    0.000    0.000 task_3.py:16(revers_1)
#      1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
run('revers_2(num)')
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#      1    0.000    0.000    0.000    0.000 task_3.py:26(revers_2)
#      1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
run('revers_3(num)')
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#      1    0.000    0.000    0.000    0.000 task_3.py:34(revers_3)
#      1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# revers_3 - Срез имеет наименьшее время т.к. используются специальные встроенные команды (BUILD_SLICE)
# и отсутствует доступ по индексу и арифметические операции
# рекурсивный вызов проигрывает циклу т.к. имеются накладные расходы на вызов функции

dis.dis(revers_1)
dis.dis(revers_2)
dis.dis(revers_3)
