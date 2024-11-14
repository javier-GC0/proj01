import requests
import time
from datetime import datetime
import logging


logging.basicConfig(
    filename="logs/project.log",
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

CRYPTO = "bitcoin"
CURRENCY = "usd"

class ApiData:
    def __init__(self, url=f"https://api.coingecko.com/api/v3/simple/price?ids={CRYPTO}&vs_currencies={CURRENCY}", interval=10, file_path="data/data.txt"):
        self.interval = interval
        self.url = url
        self.file_path = file_path
        self.logger = logging.getLogger("ApiData")

    def get_data(self):
        response = requests.get(self.url)
        price = response.json()[CRYPTO][CURRENCY]
        timestamp = datetime.now().strftime('%d-%m-%Y %H:%M:%S')
        if response.status_code == 200:
            return {"timestamp": timestamp, "price": price}
        return {}
    
    def run(self):
        self.logger.info("Starting to get data...")
        while True:
            data = self.get_data()
            if data:
                with open(self.file_path, "w", encoding="utf-8") as f:
                    f.write(f"{data["timestamp"]}; {data["price"]}")
                self.logger.info(f"Generated data - Timestamp: {data["timestamp"]}, Price: {data["price"]}")
            else:
                self.logger.warning("No data received, retrying...")
            time.sleep(self.interval)