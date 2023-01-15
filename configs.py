import logging
import os
from datetime import datetime
from logging.handlers import RotatingFileHandler
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")

BASE_DIR = Path(__file__).parent
DATETIME_FORMAT = '%Y-%m-%d_%H:%M'
DRIVER = 'driver/chromedriver.exe'
LOG_FORMAT = '"%(asctime)s - [%(levelname)s] - %(message)s"'

SCREENSHOT_DIR_URL = os.path.join(BASE_DIR, 'image')


def configure_logging():
    log_dir = BASE_DIR / 'logs'
    log_dir.mkdir(exist_ok=True)
    log_file = log_dir / 'bot.log'
    rotating_handler = RotatingFileHandler(
        log_file, maxBytes=10 ** 6, backupCount=1
    )

    logging.basicConfig(
        datefmt='%d.%m.%Y %H:%M:%S',
        format=LOG_FORMAT,
        level=logging.INFO,
        handlers=(rotating_handler,)
    )


def get_file_path(url):
    now = datetime.now()
    if 'www.' in url:
        domain_name = url.split('.')[1]
    else:
        url_name = url.split('//', 1)[1]
        domain_name = url_name.split('.', 1)[0]
    filename = f'{now.strftime(DATETIME_FORMAT)}_{domain_name}.jpg'
    file_path = os.path.join(SCREENSHOT_DIR_URL, filename)
    return file_path
