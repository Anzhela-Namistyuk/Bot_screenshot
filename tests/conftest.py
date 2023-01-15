import os
from datetime import datetime

import pytest

from configs import DATETIME_FORMAT, SCREENSHOT_DIR_URL


@pytest.fixture()
def file_path():
    now = datetime.now()
    filename = f'{now.strftime(DATETIME_FORMAT)}_youtube.jpg'
    file_path = os.path.join(SCREENSHOT_DIR_URL, filename)
    return file_path

@pytest.fixture()
def wrong_file_path():
    now = datetime.now()
    filename = f'{now.strftime(DATETIME_FORMAT)}_yotube.jpg'
    file_path = os.path.join(SCREENSHOT_DIR_URL, filename)
    return file_path

