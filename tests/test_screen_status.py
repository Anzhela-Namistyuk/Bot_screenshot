import os

import pytest

from configs import get_file_path
from screen_status import make_request, save_screenshot

TEST_UTL = 'https://www.youtube.com/'

TEST_WRONG_UTL = 'https://www.yotube'


def test_save_screenshot(file_path):
    save_screenshot(TEST_UTL, file_path)
    assert os.path.isfile(file_path)


def test_get_file_path(file_path):
    assert get_file_path(TEST_UTL) == file_path


def test_make_request():
    assert make_request(TEST_UTL) is not None
