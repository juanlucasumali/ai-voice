import sys
import pygame
import pyaudio
from audio_manager import AudioManager
from ui_manager import UIManager
from llm_manager import LLMManager
import logging
import time

# Constants
INPUT_FORMAT = pyaudio.paInt16
INPUT_CHANNELS = 1
INPUT_RATE = 16000
INPUT_CHUNK = 1024
OLLAMA_REST_HEADERS = {'Content-Type': 'application/json'}

class Uno:
    def __init__(self, config):
        self.config = config
        self.audio_manager = AudioManager(config)
        self.ui_manager = UIManager(config)
        self.llm_manager = LLMManager(config)

    def run(self):
        """
        Runs the main loop of the Uno application.
        """
        try:
            self.audio_manager.audio.open(format=INPUT_FORMAT, channels=INPUT_CHANNELS, rate=INPUT_RATE,
                            input=True, frames_per_buffer=INPUT_CHUNK).close()
        except Exception as e:
            logging.error(f"Error opening audio stream: {str(e)}")
            self.wait_exit()

        self.ui_manager.display_message(self.config.messages.loadingModel)
        self.llm_manager.ask_ollama(self.config.conversation.initial_prompt, self.audio_manager.text_to_speech)
        time.sleep(0.5)
        self.ui_manager.display_message(self.config.messages.pressSpace)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        logging.info("Push to talk key pressed")
                        logging.info("Capturing waveform from microphone")
                        self.ui_manager.display_rec_start()
                        speech = self.audio_manager.waveform_from_mic()
                        transcription = self.audio_manager.speech_to_text(speech)
                        self.llm_manager.ask_ollama(transcription, self.audio_manager.text_to_speech)
                        time.sleep(1)
                        self.ui_manager.display_message(self.config.messages.pressSpace)
                    elif event.key == pygame.K_ESCAPE:
                        logging.info("Quit key pressed")
                        self.shutdown()
                    elif event.key == pygame.K_s:
                        logging.info("Stop speech key pressed")
                        self.audio_manager.stop_speech()

    def wait_exit(self):
        """
        Waits for the user to quit the application when no audio input is available.
        """
        while True:
            self.ui_manager.display_message(self.config.messages.noAudioInput)
            pygame.time.wait(1000)
            for event in pygame.event.get(pygame.QUIT):
                self.shutdown()

    def shutdown(self):
        """
        Shuts down the Uno application and exits the program.
        """
        logging.info("Shutting down Uno")
        self.audio_manager.audio.terminate()
        pygame.quit()
        sys.exit()
