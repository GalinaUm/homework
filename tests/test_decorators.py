import os

import pytest

from src.decorators import log

LOG_FILENAME = "test_log.txt"


@pytest.fixture(autouse=True)
def cleanup_log_file():
    """Удаляет файл лога в начале и конце каждого теста"""
    if os.path.exists(LOG_FILENAME):
        os.remove(LOG_FILENAME)
    yield
    if os.path.exists(LOG_FILENAME):
        os.remove(LOG_FILENAME)


def test_log_success_console(capsys):
    @log()
    def add(a, b):
        return a + b

    result = add(2, 3)
    captured = capsys.readouterr()

    assert result == 5
    assert "add ok" in captured.out


def test_log_exception_console(capsys):
    @log()
    def fail():
        raise ValueError("fail")

    with pytest.raises(ValueError):
        fail()
    captured = capsys.readouterr()

    assert "fail error: ValueError" in captured.out
    assert "Inputs:" in captured.out


def test_log_success_file():
    @log(filename=LOG_FILENAME)
    def multiply(a, b):
        return a * b

    result = multiply(4, 5)
    assert result == 20

    with open(LOG_FILENAME, "r", encoding="utf-8") as f:
        content = f.read()
    assert "multiply ok" in content
