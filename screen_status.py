import logging
import os
from typing import Optional

import requests
from selenium import webdriver

from configs import DRIVER, configure_logging, get_file_path

configure_logging()


def save_screenshot(url: str, file_path: str):
    """Функция делает скриншот веб страницы и сохраняет его.

    Функция получает ссылку url, переходит по ней,
    делает скриншот веб страницы и сохраняет ее по
    указанному пути в file_path.
    """
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')

    options.add_argument('--no-sandbox')
    options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(executable_path=DRIVER, options=options)
    try:
        logging.info(f'Поступил url {url}')
        driver.get(url)
        logging.info(f'Получил страницу {url}')
        driver.save_screenshot(file_path)
        logging.info(f'Сделан скриншот по адресу {url}')
    except Exception as ex:
        logging.error('Ошибка', ex)
        logging.info(f'Не получилось сделать запрос по - {url}')
    finally:
        driver.quit()


def make_request(url: str) -> Optional[requests.models.Response]:
    """Функция делает запрос к сайту.

    Возвращает ответ от сайта.
    """
    try:
        response = requests.get(url)
        logging.info('Ответ получен')
        return response
    except Exception as e:
        logging.error(f'Ошибка соединения по данному URL - {url}', e)


def get_status_code(url: str) -> Optional[str]:
    """Функция делает запрос к сайту и возвращает код ответа.

    Если во время первого запроса возникла ошибка соединения
    функция сделает повторный запрос.
    """
    response = make_request(url)
    if response is None:
        response = make_request(url)
    return str(response.status_code) if response is not None else None


def is_file_exist(file_path: str) -> bool:
    """Функция проверяет существование файл по пути file_path.

    """
    return os.path.isfile(file_path)


def make_screenshot(url: str) -> Optional[str]:
    """Функция вызывает функцию save_screenshot
    и возвращает путь до файла.

    Функция вызывает функцию save_screenshot, которая
    делает скриншот страницы, проверяет если скриншота нет
    по указанному пути file_path, то вызывает повторно функцию
    save_screenshot. Если файл со скриншотом существует,
    то возвращает путь до скриншота.
    """
    file_path = get_file_path(url)
    save_screenshot(url, file_path)
    if not is_file_exist(file_path):
        save_screenshot(url, file_path)
    return file_path if is_file_exist(file_path) else None
