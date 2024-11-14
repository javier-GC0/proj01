import yaml
import logging

def load_config(config_file="config/config.yaml"):
    with open(config_file, "r") as file:
        config = yaml.safe_load(file)
    return config

CONFIG = load_config()

log_level = getattr(logging, CONFIG["logging"]["level"].upper(), logging.INFO)
logging.basicConfig(
    filename=CONFIG["logging"]["file"],
    level=log_level,
    format=CONFIG["logging"]["format"]
)