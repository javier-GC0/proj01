import logging


class LoggerConfig:
    def __init__(self, config):
        self.config = config
        log_level = getattr(logging, self.config["logging"]["level"].upper(), logging.INFO)
        logging.basicConfig(
            filename=self.config["logging"]["file"],
            level=log_level,
            format=self.config["logging"]["format"]
        )

    def get_logger(self, logger_name):
        return logging.getLogger(logger_name)