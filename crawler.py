"""
минимум 100 страниц текущего ресурса
обход в ширину или глубину
извлечь текст из страницы - почистить от html
коллекция документов
"""

"""
AdBlock похитил этот баннер, но баннеры не зубы — отрастут
"""
import requests

from bs4 import BeautifulSoup, SoupStrainer


class MyBeautifulSoup(BeautifulSoup):
    def __init__(self, *args, **kwargs):
        kwargs['features'] = 'html.parser'
        super().__init__(*args, **kwargs)


def load_document(url: str):
    """
    Загрузка документы по ссылке
    Аналог `wget`
    :param url:
    :return:
    """
    pass


def get_links(response) -> [str]:
    """
    Функция получения ссылок со страницы по ссылке
    :param url:
    :return:
    """
    links = []
    host = response.url.split('https://')[1].split('/')[0]
    # content = response.content.decode(response.encoding)
    for link in MyBeautifulSoup(response.content, parse_only=SoupStrainer('a')):
        if link.has_attr('href'):
            if link['href'].startswith(f'https://{host}/'):
                links.append(link["href"])
    return list(set(links))


def prepare_document(text):
    """
    Фукция отчистки от html тегов
    :param text:
    :return:
    """
    return ''.join(MyBeautifulSoup(text).findAll(text=True))\
        .replace('\n\n\n\n', '\n').replace('\n\n\n', '\n').replace('\n\n', '\n')


def save_to_file(name, content):
    file = open(f'index.html', 'wb')
    file.write(content.encode('utf-8'))
    file.close()


def read_from_file():
    pass


def crawler(url):
    response = requests.get(url)
    links = get_links(response)
    # assert len(links) > 100
    list(map(print, links))
    save_to_file(url, prepare_document(response.content))
    print(prepare_document(response.text))

if __name__ == '__main__':
    habra_url = 'https://habrahabr.ru/'
    crawler(habra_url)
