import pytest
from src.decorators import log


def test_log_successful_execution(capsys):
    """Тест успешного выполнения функции с выводом в консоль."""

    @log()
    def add(a: int, b: int) -> int:
        return a + b

    result = add(2, 3)
    captured = capsys.readouterr()

    assert result == 5
    assert "add ok. Result: 5" in captured.out


def test_log_with_file(tmp_path):
    """Тест логирования в файл при успешном выполнении."""
    log_file = tmp_path / "test.log"

    @log(filename=str(log_file))
    def multiply(a: int, b: int) -> int:
        return a * b

    result = multiply(4, 5)
    log_content = log_file.read_text()

    assert result == 20
    assert "multiply ok. Result: 20" in log_content


def test_log_error_case(capsys):
    """Тест обработки ошибки с выводом в консоль."""

    @log()
    def divide(a: float, b: float) -> float:
        return a / b

    with pytest.raises(ZeroDivisionError):
        divide(1, 0)

    captured = capsys.readouterr()
    assert "divide error: ZeroDivisionError" in captured.out
    assert "Inputs: (1, 0), {}" in captured.out


def test_log_error_with_file(tmp_path):
    """Тест обработки ошибки с записью в файл."""
    log_file = tmp_path / "error.log"

    @log(filename=str(log_file))
    def divide(a: float, b: float) -> float:
        return a / b

    with pytest.raises(ZeroDivisionError):
        divide(1, 0)

    log_content = log_file.read_text()
    assert "divide error: ZeroDivisionError" in log_content
    assert "Inputs: (1, 0), {}" in log_content
