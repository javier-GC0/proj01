import time
from file_handler import FileHandler
from logging_handler import LoggerConfig


class DataClient():
    def __init__(self, config):
        self.config = config
        self.file_path = self.config["data_file"]["path"]
        self.last_timestamp = None
        self.poll_interval = self.config["intervals"]["poll_interval"]
        self.file_handler = FileHandler(self.config["data_file"]["path"], self.config)
        logger_config = LoggerConfig(self.config) 
        self.logger = logger_config.get_logger(self.config["logging"]["client_name"])
    
    def check_new_data(self):
        try:
            line = self.file_handler.read_data()
            timestamp, price = line.split(self.config["data_file"]["delimiter"])
            if timestamp != self.last_timestamp:
                self.last_timestamp = timestamp
                self.logger.info(f"New data - Timestamp: {timestamp}, Price:{price}")
        except FileNotFoundError:
            self.logger.error("Data file not found.")
        except Exception as e:
            self.logger.error(f"Error reading data: {e}")

    def run(self):
        self.logger.info("Starting client polling...")
        while True:
            self.check_new_data()
            time.sleep(self.poll_interval)