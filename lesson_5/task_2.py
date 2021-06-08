"""
2. Написать программу сложения и умножения двух шестнадцатиричных чисел.
При этом каждое число представляется как массив, элементы которого это цифры числа.
Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
Подсказка:
Для решения задачи обязательно примените какую-нибудь коллекцию из модуля collections
Для лучшее освоения материала можете даже сделать несколько решений этого задания,
применив несколько коллекций из модуля collections
Также попробуйте решить задачу вообще без collections и применить только ваши знания по ООП
(в частности по перегрузке методов)
__mul__
__add__
Пример:
Например, пользователь ввёл A2 и C4F.
Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’]
Произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
1. вариант
defaultdict(list)
int(, 16)
reduce
2. вариант
class HexNumber:
    __add__
    __mul__
hx = HexNumber
hx + hx
hex()
"""

from collections import defaultdict
from functools import reduce


def read_hex_str(msg) -> str:
    while True:
        hex_str = input(msg)
        try:
            int(hex_str, 16)
            return hex_str
        except ValueError:
            print(f"Incorrect hex number {hex_str}")


# Option 1
def collections_test():
    hex_numbers = defaultdict(list)
    first = read_hex_str("Input first number: ")
    second = read_hex_str("Input second number: ")
    first_int = int(first, 16)
    second_int = int(second, 16)
    for s in first:
        hex_numbers[first_int].append(s)
    for s in second:
        hex_numbers[second_int].append(s)

    print(f"First number: {hex_numbers[first_int]}")
    print(f"Second number: {hex_numbers[second_int]}")

    sum_list = [char for char in format(reduce(lambda x, y: x + y, hex_numbers), 'x')]
    mul_list = [char for char in format(reduce(lambda x, y: x * y, hex_numbers), 'x')]

    print(f"Sum of numbers: {sum_list}")
    print(f"Mul of numbers: {mul_list}")


# Option 2
class HexNumber:
    def __init__(self, hex_str):
        self.hex_list = [char for char in hex_str]
        self.num = int(hex_str, 16)

    def __add__(self, hex_num):
        hex_sum = self.num + hex_num.num
        return HexNumber(format(hex_sum, 'x'))

    def __mul__(self, hex_num):
        hex_sum = self.num * hex_num.num
        return HexNumber(format(hex_sum, 'x'))

    def __str__(self):
        return hex(self.num)

    def as_list(self):
        return self.hex_list


first_number = HexNumber(read_hex_str("Input first number: "))
second_number = HexNumber(read_hex_str("Input second number: "))

print(f"First number is: {first_number.as_list()}")
print(f"Second number is: {second_number.as_list()}")
print(f"Sum of numbers: {(first_number + second_number).as_list()}")
print(f"Mul of numbers: {(first_number * second_number).as_list()}")

collections_test()
