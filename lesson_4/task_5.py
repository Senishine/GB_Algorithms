"""
Задание 5.**
Приведен наивный алгоритм нахождения i-го по счёту
простого числа (через перебор делителей).
Попробуйте решить эту же задачу,
применив алгоритм "Решето Эратосфена" (https://younglinux.info/algorithm/sieve)
Подсказка:
Сравните алгоритмы по времени на разных порядковых номерах чисел:
10, 100, 1000
Опишите результаты, сделайте выводы, где и какой алгоритм эффективнее
Подумайте и по возможности определите сложность каждого алгоритма.
Укажите формулу сложности О-нотация каждого алгоритма
и сделайте обоснование результатам.
"""
import timeit


def simple(i):  # O(n^2)
    """Без использования «Решета Эратосфена»"""
    count = 1
    n = 2
    while count <= i:
        t = 1
        is_simple = True
        while t <= n:
            if n % t == 0 and t != 1 and t != n:
                is_simple = False
                break
            t += 1
        if is_simple:
            if count == i:
                break
            count += 1
        n += 1
    return n


def sieve(i):  # O(n log(log(n)))
    if i == 1:
        return 2
    if i == 2:
        return 3
    primes = [2, 3]
    count = 3
    n = 5
    while count <= i:
        is_simple = True
        for p in primes[0:len(primes) // 2]:
            if n % p == 0:
                is_simple = False
                break
        if is_simple:
            primes.append(n)
            count += 1
        n += 2
    return primes[len(primes) - 1]


i = int(input('Введите порядковый номер искомого простого числа: '))
naive_alg = simple(i)
sieve_alg = sieve(i)
print(f"naive: {naive_alg}")
print(f"sieve: {sieve_alg}")
assert naive_alg == sieve_alg

print(f"naive: {timeit.timeit(lambda: simple(i), number=1000)}")
print(f"sieve: {timeit.timeit(lambda: sieve(i), number=1000)}")

# Введите порядковый номер искомого простого числа: 157
# naive: 919
# sieve: 919
# naive: 6.057368500000001
# sieve: 0.6447342999999996


# Поиск по алгоритму "Решето Эратосфена" работает намного быстрее т.к. имеет меньшую алгоритмическую сложность
# Так как не требуется перебор всех чисел, а только простых меньше очередного i-того
# Количество простых чисел по отношению ко всем натуральным равно n/log(n),
# а сложность всего алгоритма оценивается как n log(log(n)), что существенно меньше чем n^2
