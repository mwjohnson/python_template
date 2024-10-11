import sys
import logging
import colorlog

class LevelBasedFormatter(logging.Formatter):
    # Define formats for different log levels
    FORMATS = {
        logging.DEBUG: "%(log_color)s%(levelname)s: [%(filename)s:%(lineno)d]: %(message)s",
        logging.INFO: "%(log_color)s%(levelname)s: [%(filename)s:%(lineno)d]: %(message)s",
        logging.WARNING: "%(log_color)s%(levelname)s: %(asctime)s [%(name)s:%(filename)s:%(funcName)s:%(lineno)d]: %(message)s",
        logging.ERROR: "%(log_color)s%(levelname)s: %(asctime)s [%(name)s:%(filename)s:%(funcName)s:%(lineno)d]: %(message)s",
        logging.CRITICAL: "%(log_color)s%(levelname)s: %(asctime)s [%(name)s:%(filename)s:%(funcName)s:%(lineno)d]: %(message)s"
    }

    # Define colors for different log levels
    LOG_COLORS = {
        'DEBUG': 'green',
        'INFO': 'blue',
        'WARNING': 'yellow',
        'ERROR': 'red',
        'CRITICAL': 'bold_red',
    }

    def format(self, record):
        # Select the format based on the log level
        log_fmt = self.FORMATS.get(record.levelno, self.FORMATS[logging.INFO])
        formatter = colorlog.ColoredFormatter(
            log_fmt,
            datefmt='%Y-%m-%d %H:%M:%S',
            log_colors=self.LOG_COLORS
        )
        return formatter.format(record)

def setup_custom_logger(name: str, log_to_file: bool = False):
    ologger = logging.getLogger(name)
    print(f'created new logger: {ologger.name}')
    ologger.setLevel(logging.DEBUG)  # Set the lowest level to capture all messages

    # Create handler (console in this case)
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(logging.DEBUG)  # Set handler level to the lowest

    # Apply the custom formatter to the handler
    formatter = LevelBasedFormatter()
    console_handler.setFormatter(formatter)

    if log_to_file:
        file_handler = logging.FileHandler('./debug.log')  # ログファイルに出力するHandlerの設定
        file_handler.setFormatter(formatter)

    # Avoid adding multiple handlers if the logger already has them
    if not ologger.handlers:
        ologger.addHandler(console_handler)
        if log_to_file:
            ologger.addHandler(file_handler)

    ologger.propagate = False
    return ologger


class LevelBasedFormatterV1(logging.Formatter):
    # Define formats for different log levels
    FORMATS = {
        logging.DEBUG: "%(levelname)s: %(message)s",
        logging.INFO: "%(levelname)s: %(message)s",
        logging.WARNING: "%(levelname)s %(asctime)s [%(name)s:%(filename)s:%(funcName)s:%(lineno)d]: %(message)s",
        logging.ERROR: "%(levelname)s: %(asctime)s [%(name)s:%(filename)s:%(funcName)s:%(lineno)d]: %(message)s",
        logging.CRITICAL: "%(levelname)s: %(asctime)s [%(name)s:%(filename)s:%(funcName)s:%(lineno)d]: %(message)s"
    }

    def format(self, record):
        # Select the format based on the log level
        log_fmt = self.FORMATS.get(record.levelno, self.FORMATS[logging.INFO])
        formatter = logging.Formatter(log_fmt, datefmt='%Y-%m-%d %H:%M:%S')
        return formatter.format(record)

def main():
    logger.info(__name__ + " started.")
    # input_file = './japan-ai-incident/2024-05-30.json'
    # process_log(input_file)
    # find_service_files('./japan-ai-incident/')
    # gather_text('./japan-ai-incident/')

    logger.debug("This is a DEBUG message.")
    logger.info("This is an INFO message.")
    logger.warning("This is a WARNING message.")
    logger.error("This is an ERROR message.")
    logger.critical("This is a CRITICAL message.")

    logger.info('Complete.')


if __name__ == '__main__':
    logger = setup_custom_logger(__name__, False)
    main()
