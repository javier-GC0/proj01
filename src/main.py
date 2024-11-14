import threading
import sys
import os
from client import DataClient
from get_data import ApiData

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from setup import CONFIG


class Main:
    def __init__(self, data_class, client_class):
        self.data_class = data_class
        self.client_class = client_class

    def start(self):
        data_thread = threading.Thread(target=self.data_class.run)
        client_thread = threading.Thread(target=self.client_class.run)

        data_thread.start()
        client_thread.start()

        data_thread.join()
        client_thread.join()

if __name__ == "__main__":
    data_instance = ApiData(CONFIG)
    client_instance = DataClient(CONFIG)
    main_instance = Main(data_instance, client_instance)

    main_instance.start()