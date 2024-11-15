import requests
import time
from datetime import datetime
from file_handler import FileHandler
from logging_handler import LoggerConfig

class ApiData:
    def __init__(self, config):
        self.config = config
        self.url = self.config["api_info"]["url"].format(crypto=self.config["api_info"]["crypto"], currency=self.config["api_info"]["currency"])
        self.interval = self.config["intervals"]["interval"]
        self.file_path = self.config["data_file"]["path"]
        self.file_handler = FileHandler(self.config["data_file"]["path"], self.config)
        logger_config = LoggerConfig(self.config) 
        self.logger = logger_config.get_logger(self.config["logging"]["data_name"])

    def get_data(self):
        response = requests.get(self.url)
        try:
            data = response.json()
            fact = data["fact"]
            timestamp = datetime.now().strftime(self.config["data_file"]["date_format"])
            if response.status_code == 200:
                return {"timestamp": timestamp, "fact": fact}
        except Exception as e:
            self.logger.error(f"Error obtaining or processing data: {e}")
            return {}
    
    def run(self):
        self.logger.info("Starting to get data...")
        while True:
            data = self.get_data()
            if data:
                self.file_handler.write_data(data)
                self.logger.info(f"Generated data - Timestamp: {data["timestamp"]}, Fact: {data["fact"]}")
            else:
                self.logger.warning("No data received, retrying...")
            time.sleep(self.interval)