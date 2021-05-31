"""
2.	Посчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, то у него 3 четные цифры
(4, 6 и 0) и 2 нечетные (3 и 5).
Подсказка:
На каждом шаге вам нужно 'доставать' из числа очередную цифру
и смотреть является ли она четной или нечетной. При этом увеличиваем соответствующий счетчик
Пока все числа не извлечены рекурсивные вызовы продолжаем
Условие завершения рекурсии - все числа извлечены
Используем операции % //, НЕ ИСПОЛЬЗУЕМ ОПЕРАЦИИ ВЗЯТИЯ ЭЛЕМЕНТА ПО ИНДЕКСУ
Пример:
Введите число: 123
Количество четных и нечетных цифр в числе равно: (1, 2)
Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
"""


class NumberResult:
    def __init__(self, even, odd):
        self.even = even
        self.odd = odd

    def __str__(self) -> str:
        return f'even: {self.even}, odd: {self.odd}'

    def __add__(self, other):
        return NumberResult(self.even + other.even, self.odd + other.odd)

    @staticmethod
    def from_string(source):
        return NumberResult.__check_number__(int(source))

    @staticmethod
    def __check_number__(num):
        num = abs(num)
        result = NumberResult(1, 0) if (num % 10) % 2 == 0 else NumberResult(0, 1)
        if num >= 10:
            return result + NumberResult.__check_number__(num // 10)
        return result


print(NumberResult.from_string(input("Input the number: ")))
