import requests
import time
from datetime import datetime
import logging


logging.basicConfig(
    filename="logs/project.log",
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)


class ApiData:
    def __init__(self, url="https://catfact.ninja/fact", interval=10, file_path="data/data.txt"):
        self.interval = interval
        self.url = url
        self.file_path = file_path
        self.logger = logging.getLogger("ApiData")

    def get_data(self):
        response = requests.get(self.url)
        fact = response.json()["fact"]
        timestamp = datetime.now().strftime('%d-%m-%Y %H:%M:%S')
        return {"timestamp": timestamp, "cats_fact": fact}
    
    def run(self):
        self.logger.info("Starting to get data...")
        while True:
            data = self.get_data()
            with open(self.file_path, "w", encoding="utf-8") as f:
                f.write(f"{data["timestamp"]}; {data["cats_fact"]}")
            self.logger.info(f"Generated data - Timestamp: {data["timestamp"]}, Fact: {data["cats_fact"]}")
            time.sleep(self.interval)