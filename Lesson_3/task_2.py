"""
Задание 2.
Ваша программа должна запрашивать пароль
Для этого пароля вам нужно получить хеш, используя функцию sha256
Для генерации хеша обязательно нужно использовать криптографическую соль
Обязательно выведите созданный хеш.
Далее программа должна запросить пароль повторно
Вам нужно проверить, совпадает ли пароль с исходным
Для проверки необходимо сравнить хеши паролей
ПРИМЕР:
Введите пароль: 123
В базе данных хранится строка: 555a3581d37993843efd4eba1921f1dcaeeafeb855965535d77c55782349444b
Введите пароль еще раз для проверки: 123
Вы ввели правильный пароль
Обязательно усложните задачу! Добавьте сохранение хеша в файле и получение его из файла.
А если вы знаете как через Python работать с БД, привяжите к заданию БД и сохраняйте хеши там.
"""
import uuid
import hashlib
import sqlite3
from sqlite3 import Connection

create_table = """
CREATE TABLE IF NOT EXISTS accounts (
    login_id text NOT NULL,
    pwd_hash text,
    salt text);
"""


class Credentials:
    def __init__(self, pwd_hash_256, salt):
        self.pwd_hash_256 = pwd_hash_256
        self.salt = salt


class Account:
    def __init__(self, user_name, credentials):
        self.user_name = user_name
        self.credentials = credentials

    def __str__(self) -> str:
        return f'Account [user_name: {self.user_name}, password hash: {self.credentials.pwd_hash_256.hex()}]'


def __input_string__(name: str, min_len: int):
    result = input(f'Please input {name}: ')
    while len(result) < min_len:
        print(f'{name} cannot be less than {min_len} symbols')
        result = input(f'Please input {name}: ')
    return result


def sign_in(conn: Connection):
    cur = conn.cursor()
    try:
        while True:
            rows = cur.execute('SELECT login_id FROM accounts').fetchall()
            user_name = __input_string__('user name', 3).lower()
            user_found = False
            for row in rows:
                if user_name == str(row[0]).lower():
                    print(f'User name is already exists [name={user_name}]')
                    user_found = True
                    break
            if not user_found:
                break
        password = __input_string__('password', 8).encode('utf-8')
        salt = uuid.uuid4().bytes
        hash_obj = hashlib.sha256()
        hash_obj.update(password)
        hash_obj.update(salt)
        credentials = Credentials(hash_obj.digest(), salt)
        account = Account(user_name, credentials)
        cur.execute(
            'INSERT INTO accounts(login_id, pwd_hash, salt) VALUES(?,?,?)',
            (account.user_name, credentials.pwd_hash_256.hex(), credentials.salt.hex())
        )
        conn.commit()
        return account
    finally:
        cur.close()


def log_in(conn: Connection) -> str:
    user_name = __input_string__('user name', 3).lower()
    password = __input_string__('password', 8).encode('utf-8')

    cur = conn.cursor()
    try:
        row = cur.execute('SELECT login_id, pwd_hash, salt FROM accounts WHERE login_id=?', (user_name,)).fetchone()
        if row is None:
            return f'There is no such user {user_name}'
        acc = Account(row[0], Credentials(bytearray.fromhex(row[1]), bytearray.fromhex(row[2])))
        hash_obj = hashlib.sha256()
        hash_obj.update(password)
        hash_obj.update(acc.credentials.salt)

        if hash_obj.digest() != acc.credentials.pwd_hash_256:
            return 'Password is incorrect'
        return 'Access granted'
    finally:
        cur.close()


if __name__ == '__main__':
    connection = None
    try:
        connection = sqlite3.connect('./accounts.db')
        cursor = connection.cursor()
        cursor.execute(create_table)
        cursor.close()

        print(f'User created: {sign_in(connection)}')
        print(f'Login result: {log_in(connection)}')
    finally:
        if connection is not None:
            connection.close()
