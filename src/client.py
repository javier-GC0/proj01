import requests
import time
import datetime
import logging


logging.basicConfig(
    filename="project.log",
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)


class DataClient():
    def __init__(self, interval=2, file_path="facts_data.txt"):
        self.file_path = file_path
        self.interval = interval
        self.logger = logging.getLogger("DataClient")
    
    def check_new_data(self):
        try:
            with open(self.file_path, "r") as f:
                line = f.readline().strip()
                timestamp, fact = line.split(",")
                if timestamp != self.last_timestamp:
                    self.last_timestamp = timestamp
                    self.logger.info(f"New fact - Timestamp: {timestamp}, Fact: {fact}")
        except FileNotFoundError:
            self.logger.error("Data file not found.")
        except Exception as e:
            self.logger.error(f"Error reading data: {e}")

    def run(self):
        self.logger.info("Starting client polling...")
        while True:
            self.check_new_data()
            time.sleep(self.interval)