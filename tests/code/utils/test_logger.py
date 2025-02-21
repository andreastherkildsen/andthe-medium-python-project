import os

from src.code.utils.logger import Logger


def test_logger_default_log() -> None:
    test_message = "Test message"
    Logger.log(Logger, test_message, Logger.default_log)
    log_file_path = os.path.join(Logger.logs_dir, Logger.default_log)

    assert os.path.exists(log_file_path)

    with open(log_file_path) as file:
        content = file.read()
        assert test_message in content


def test_logger_custom_log() -> None:
    custom_log_file = "test-logger.log"
    test_message = "Test message is present in log"

    Logger.log(Logger, test_message, file_name=custom_log_file)
    log_file_path = os.path.join(Logger.logs_dir, custom_log_file)

    assert os.path.exists(log_file_path)

    with open(log_file_path) as file:
        content = file.read()
        assert test_message in content
