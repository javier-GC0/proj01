
class FileHandler:
    def __init__(self, file_path, config):
        self.file_path = file_path
        self.config = config

    def write_data(self, data):
        with open(self.file_path, "w", encoding=self.config["data_file"]["encoding"]) as f:
            f.write(f"{data["timestamp"]}{self.config["data_file"]["delimiter"]} {data["fact"]}")

    def read_data(self):
        with open(self.file_path, "r", encoding=self.config["data_file"]["encoding"]) as f:
            return f.readline().strip()