"""
1.	Пользователь вводит данные о количестве предприятий, их наименования и прибыль
за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия.
Программа должна определить среднюю прибыль (за год для всех предприятий)
и вывести наименования предприятий, чья прибыль выше среднего и отдельно
вывести наименования предприятий, чья прибыль ниже среднего.
Подсказка:
Для решения задачи обязательно примените какую-нибудь коллекцию из модуля collections.
Пример:
Введите количество предприятий для расчета прибыли: 2
Введите название предприятия: Фирма_1
через пробел введите прибыль данного предприятия
за каждый квартал(Всего 4 квартала): 235 345634 55 235
Введите название предприятия: Фирма_2
через пробел введите прибыль данного предприятия
за каждый квартал(Всего 4 квартала): 345 34 543 34
Средняя годовая прибыль всех предприятий: 173557.5
Предприятия, с прибылью выше среднего значения: Фирма_1
Предприятия, с прибылью ниже среднего значения: Фирма_2
"""

from collections import defaultdict


def read_firms_count() -> int:
    value = 0
    while value <= 0:
        try:
            value = int(input("Input firms count: "))
            if value <= 0:
                print(f"Value must be greater than zero [enteredValue={value}]")
                continue
        except ValueError:
            print(f"Incorrect number [enteredValue={value}]")
    return value


def read_firm_name() -> str:
    return input("Input firm name: ")


def read_quarter_income() -> list:
    while True:
        value = input("Input income with spaces e.g. 245 34 543 34: ")
        result = value.split(" ")
        if len(result) != 4:
            print("You entered incorrect income values")
            continue
        try:
            return list(map(lambda x: int(x), result))
        except ValueError:
            continue


firms_count = read_firms_count()
total_income = 0
firm_income_dict = defaultdict(int)
for i in range(0, firms_count):
    firm_name = read_firm_name()
    quarter_incomes = read_quarter_income()
    for idx, income in enumerate(quarter_incomes):
        firm_income_dict[firm_name] += income
        total_income += income

average = total_income / firms_count
less_than_avg = set(map(lambda entry: entry[0], filter(lambda entry: entry[1] < average, firm_income_dict.items())))
greater_than_avg = set(filter(lambda key: key not in less_than_avg, firm_income_dict.keys()))
print(f"Average firms income: {average}")
print(f"Firms with income less than average: {less_than_avg}")
print(f"Firms with income greater than average: {greater_than_avg}")


