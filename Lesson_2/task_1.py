"""
1.	Написать программу, которая будет складывать, вычитать, умножать или делить
два числа. Числа и знак операции вводятся пользователем. После выполнения
вычисления программа не должна завершаться, а должна запрашивать новые данные
для вычислений. Завершение программы должно выполняться при вводе символа '0'
в качестве знака операции. Если пользователь вводит неверный знак
(не '0', '+', '-', '*', '/'), то программа должна сообщать ему об ошибке и
снова запрашивать знак операции.
Также сообщать пользователю о невозможности деления на ноль,
если он ввел 0 в качестве делителя.
Подсказка:
Вариант исполнения:
- условие рекурсивного вызова - введена операция +, -, *, / - ШАГ РЕКУРСИИ
- условие завершения рекурсии - введена операция 0 - БАЗОВЫЙ СЛУЧАЙ
Пример:
Введите операцию (+, -, *, / или 0 для выхода): +
Введите первое число: 214
Введите второе число: 234
Ваш результат 448
Введите операцию (+, -, *, / или 0 для выхода): -
Введите первое число: вп
Вы вместо трехзначного числа ввели строку (((. Исправьтесь
Введите операцию (+, -, *, / или 0 для выхода):
Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
"""
operations = {
    '0': lambda left, right: None,
    '+': lambda left, right: left + right,
    '-': lambda left, right: left - right,
    '*': lambda left, right: left * right,
    '/': lambda left, right: left / right}


def read_number(message):
    source = ''
    try:
        source = input(message)
        return float(source)
    except ValueError:
        print(f'Incorrect number {source}, try again please')
        return read_number(message)


def read_operation():
    source = input('Input operation +, -, *, / or 0 to exit: ')
    if source in operations.keys():
        return source
    print(f'You entered not valid operation [expected={operations.keys()}, entered={source}]')
    return read_operation()


def __calculate_inner__(first, operation, second):
    if operation == '0':
        print(f'Calculation stopped, user entered 0')
        return
    if first is None:
        __calculate_inner__(read_number('Input first number: '), operation, second)
        return
    if operation is None:
        __calculate_inner__(first, read_operation(), second)
        return
    if second is None:
        __calculate_inner__(first, operation, read_number('Input second number: '))
        return
    try:
        print(operations[operation](first, second))
    except ZeroDivisionError:
        print("can't divide by zero'")
    __calculate_inner__(None, None, None)


def calculate():
    return __calculate_inner__(None, None, None)


calculate()
