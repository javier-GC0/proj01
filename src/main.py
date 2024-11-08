import threading
from client import DataClient
from get_data import ApiData


def main():
    data = ApiData()
    client = DataClient()

    data_thread = threading.Thread(target=data.run)
    client_thread = threading.Thread(target=client.run)

    data_thread.start()
    client_thread.start()

    data_thread.join()
    client_thread.join()

if __name__ == "__main__":
    main()