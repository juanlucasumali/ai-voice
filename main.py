import yaml
import logging
import pygame
from uno import Uno

# Constants
INPUT_CONFIG_PATH = "uno.yaml"

# Configure logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

class Config:
    def __init__(self, config_yaml):
        self.messages = type('', (), config_yaml["messages"])()
        self.conversation = type('', (), config_yaml["conversation"])()
        self.ollama = type('', (), config_yaml["ollama"])()
        self.whisperRecognition = type('', (), config_yaml["whisperRecognition"])()
        self.ui = type('', (), config_yaml["ui"])()

def main():
    logging.info("Starting Uno")
    pygame.init()
    with open(INPUT_CONFIG_PATH, encoding='utf-8') as data:
        config_yaml = yaml.safe_load(data)
    config = Config(config_yaml)

    uno = Uno(config)
    uno.run()

if __name__ == "__main__":
    main()