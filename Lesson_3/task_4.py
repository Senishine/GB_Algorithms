"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"
Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если нет, то вносить ее в кэш
Подсказка: задачу решите обязательно с применением 'соленого' хеширования и хеш-таблиц
Можете условжнить задачу, реализовав ее через ООП
Не забудьте, что кэширование - механизм, а хеш-таблица - средство его реализации.
Задание творческое. Здесь нет жестких требований к выполнению.
"""

from uuid import uuid4
from hashlib import sha256


class WebServer:
    def __init__(self, page_loader):
        self.salt = uuid4().bytes
        self.page_loader = page_loader
        self.dict = {}

    def get_page(self, url: str) -> str:
        hash_obj = sha256()
        hash_obj.update(url.encode('utf-8'))
        hash_obj.update(self.salt)
        key = hash_obj.hexdigest()
        page = self.dict.get(key)
        if page is None:
            page = self.page_loader(url)
            self.dict[key] = page
            print(f'Page added to cache [key={key}, value={page}]')
        else:
            print(f'Page has been taken from cache [key={key}, value={page}]')
        return page


def generate_page(url) -> str:
    return f"""
    <html>
        <head>
            <title>{url}</title>
        </head>
        <body>
            <div>This page loaded for url {url}</div>
            <div>Unique page id {uuid4().hex}</div>
        </body>
    </html>
    """


def load_test_urls(ws):
    ws.get_page('https://vk.com')
    ws.get_page('https://google.com')
    ws.get_page('https://geekbrains.com')
    ws.get_page('https://jetbrains.com')
    ws.get_page('https://habr.com')
    ws.get_page('https://youtube.com')
    ws.get_page('https://tiktok.com')


web_server = WebServer(generate_page)
load_test_urls(web_server)
load_test_urls(web_server)
