"""
Задание 3.
Определить количество различных (уникальных) подстрок с использованием хеш-функции.
Дана строка S длиной N, состоящая только из строчных латинских букв.
Подсказка: примените вычисление хешей для подстрок с помощью хеш-функций и множества
Можно воспользоваться ф-цией hash() (см. материалы к уроку)
Пример:
рара - 6 уникальных подстрок
рар
ра
ар
ара
р
а
"""


def simple_algorithm(text: str):
    result = set()
    for i in range(1, len(text)):
        for j in range(0, len(text) - i + 1):
            # result.add(hash(text[j:(j + i)])) - нельзя тк
            result.add(text[j:(j + i)])
    return len(result)


def hash_algorithm(text: str):
    arr = [set() for _ in range(0, max(len(text), 16))]
    buckets_count = len(arr)
    for i in range(1, len(text)):
        for j in range(0, len(text) - i + 1):
            substring = text[j:(j + i)]
            index = hash(substring) % buckets_count
            arr[index].add(substring)
    return sum(map(lambda x: len(x), arr))


test_string = input('Input the string: ')
print(f'substrings number (simple): {simple_algorithm(test_string)}')
print(f'substrings number (hash): {hash_algorithm(test_string)}')
