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

# import sys
# import json
# import time
# import pyttsx3
# import torch
# import requests
# import yaml
# import pygame
# import numpy as np
# import pyaudio
# import whisper
# import logging
# import threading
# import queue

# from typing import Callable

# # Configure logging
# logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# # Constants
# BACK_COLOR = (0, 0, 0)
# REC_COLOR = (255, 188, 107)
# TEXT_COLOR = (255, 255, 255)
# REC_SIZE = 80
# FONT_SIZE = 24
# WIDTH, HEIGHT = 320, 240
# KWIDTH, KHEIGHT = 20, 6
# MAX_TEXT_LEN_DISPLAY = 32

# INPUT_FORMAT = pyaudio.paInt16
# INPUT_CHANNELS = 1
# INPUT_RATE = 16000
# INPUT_CHUNK = 1024
# OLLAMA_REST_HEADERS = {'Content-Type': 'application/json'}
# INPUT_CONFIG_PATH = "uno.yaml"

# class Config:
#     def __init__(self, config_yaml):
#         self.messages = type('', (), config_yaml["messages"])()
#         self.conversation = type('', (), config_yaml["conversation"])()
#         self.ollama = type('', (), config_yaml["ollama"])()
#         self.whisperRecognition = type('', (), config_yaml["whisperRecognition"])()

# class Uno:
#     def __init__(self, config: Config):
#         """
#         Initializes the Uno class with the given configuration.

#         Args:
#             config (Config): The configuration object containing settings for the application.
#         """
#         logging.info("Initializing Uno")
#         self.config = config

#         pygame.display.set_icon(pygame.image.load('uno.png'))
#         pygame.display.set_caption("Uno")

#         self.windowSurface = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)
#         self.font = pygame.font.SysFont(None, FONT_SIZE)

#         self.audio = pyaudio.PyAudio()
#         self.engine = pyttsx3.init()
#         self.engine.setProperty('rate', self.engine.getProperty('rate'))

#         self.model = whisper.load_model(self.config.whisperRecognition.modelPath)
#         self.context = []

#     def run(self):
#         """
#         Runs the main loop of the Uno application.
#         """
#         try:
#             
# .open(format=INPUT_FORMAT, channels=INPUT_CHANNELS, rate=INPUT_RATE,
#                             input=True, frames_per_buffer=INPUT_CHUNK).close()
#         except Exception as e:
#             logging.error(f"Error opening audio stream: {str(e)}")
#             self.wait_exit()

#         self.display_message(self.config.messages.loadingModel)
#         self.ask_ollama(self.config.conversation.initial_prompt, self.text_to_speech)
#         time.sleep(0.5)
#         self.display_message(self.config.messages.pressSpace)

#         while True:
#             for event in pygame.event.get():
#                 if event.type == pygame.KEYDOWN:
#                     if event.key == pygame.K_SPACE:
#                         logging.info("Push to talk key pressed")
#                         speech = self.waveform_from_mic()
#                         transcription = self.speech_to_text(speech)
#                         self.ask_ollama(transcription, self.text_to_speech)
#                         time.sleep(1)
#                         self.display_message(self.config.messages.pressSpace)
#                     elif event.key == pygame.K_ESCAPE:
#                         logging.info("Quit key pressed")
#                         self.shutdown()
#                     elif event.key == pygame.K_s:
#                         logging.info("Stop speech key pressed")
#                         self.stop_speech()

#     def wait_exit(self):
#         """
#         Waits for the user to quit the application when no audio input is available.
#         """
#         while True:
#             self.display_message(self.config.messages.noAudioInput)
#             pygame.time.wait(1000)
#             for event in pygame.event.get(pygame.QUIT):
#                 self.shutdown()

#     def shutdown(self):
#         """
#         Shuts down the Uno application and exits the program.
#         """
#         logging.info("Shutting down Uno")
#         self.audio.terminate()
#         pygame.quit()
#         sys.exit()

#     def stop_speech(self):
#         """
#         Stops the current speech playback.
#         """
#         logging.info("Stopping speech")
#         self.engine.stop()
#         logging.info("Stopped speech")

#     def display_message(self, text: str):
#         """
#         Displays a message on the Uno application window.

#         Args:
#             text (str): The message text to be displayed.
#         """
#         logging.info(f"Displaying message: {text}")
#         self.windowSurface.fill(BACK_COLOR)

#         text = text[:MAX_TEXT_LEN_DISPLAY] + "..." if len(text) > MAX_TEXT_LEN_DISPLAY else text
#         label = self.font.render(text, 1, TEXT_COLOR)
#         size = label.get_rect()[2:4]
#         self.windowSurface.blit(label, (WIDTH // 2 - size[0] // 2, HEIGHT // 2 - size[1] // 2))

#         pygame.display.flip()

#     def waveform_from_mic(self, key=pygame.K_SPACE) -> np.ndarray:
#         """
#         Captures audio waveform from the microphone while the specified key is pressed.

#         Args:
#             key (int): The key code of the key to be pressed for audio capture (default: pygame.K_SPACE).

#         Returns:
#             np.ndarray: The captured audio waveform as a numpy array.
#         """
#         logging.info("Capturing waveform from microphone")
#         self.display_rec_start()

#         stream = self.audio.open(format=INPUT_FORMAT, channels=INPUT_CHANNELS, rate=INPUT_RATE,
#                                  input=True, frames_per_buffer=INPUT_CHUNK)
#         frames = []

#         while pygame.key.get_pressed()[key]:
#             pygame.event.pump()
#             frames.append(stream.read(INPUT_CHUNK))

#         stream.stop_stream()
#         stream.close()

#         return np.frombuffer(b''.join(frames), np.int16).astype(np.float32) * (1 / 32768.0)

#     def speech_to_text(self, waveform: np.ndarray) -> str:
#         """
#         Converts speech audio waveform to text using the Whisper model.

#         Args:
#             waveform (np.ndarray): The audio waveform to be transcribed.

#         Returns:
#             str: The transcribed text from the audio waveform.
#         """
#         logging.info("Converting speech to text")
#         result_queue = queue.Queue()

#         def transcribe_speech():
#             try:
#                 logging.info("Starting transcription")
#                 transcript = self.model.transcribe(waveform, language=self.config.whisperRecognition.lang,
#                                                    fp16=torch.cuda.is_available())
#                 logging.info("Transcription completed")
#                 text = transcript["text"]
#                 print('\nYOU:\n', text.strip())
#                 result_queue.put(text)
#             except Exception as e:
#                 logging.error(f"An error occurred during transcription: {str(e)}")
#                 result_queue.put("")

#         threading.Thread(target=transcribe_speech).start()
#         return result_queue.get()

#     def ask_ollama(self, prompt: str, response_callback: Callable[[str], None]):
#         """
#         Sends a prompt to the Ollama API and returns the generated response from the LLM.

#         Args:
#             prompt (str): The input text to be processed by the LLM.
#             response_callback (Callable[[str], None]): A callback function to handle the generated response.
#         """
#         logging.info(f"Asking OLLaMa with prompt: {prompt}")
#         full_prompt = prompt if hasattr(self, "contextSent") else prompt
#         self.contextSent = True
#         jsonParam = {
#             "model": self.config.ollama.model,
#             "stream": True,
#             "context": self.context,
#             "prompt": full_prompt
#         }

#         try:
#             response = requests.post(self.config.ollama.url, json=jsonParam, headers=OLLAMA_REST_HEADERS,
#                                      stream=True, timeout=30)
#             response.raise_for_status()

#             full_response = ""
#             for line in response.iter_lines():
#                 body = json.loads(line)
#                 token = body.get('response', '')
#                 full_response += token

#                 if 'error' in body:
#                     logging.error(f"Error from OLLaMa: {body['error']}")
#                     response_callback("Error: " + body['error'])
#                     return

#                 if body.get('done', False) and 'context' in body:
#                     self.context = body['context']
#                     break

#             response_callback(full_response.strip())

#         except requests.exceptions.RequestException as e:
#             logging.error(f"An error occurred while asking OLLaMa: {str(e)}")
#             response_callback("Sorry, an error occurred. Please try again.")

#     def text_to_speech(self, text: str):
#         """
#         Converts text to speech using the pyttsx3 engine.

#         Args:
#             text (str): The text to be converted to speech.
#         """
#         logging.info(f"Converting text to speech: {text}")
#         print('\nUNO:\n', text.strip())

#         def play_speech():
#             try:
#                 logging.info("Converting text to speech")
#                 self.engine.say(text)
#                 self.engine.runAndWait()
#                 logging.info("Speech playback completed")
#             except Exception as e:
#                 logging.error(f"An error occurred during speech playback: {str(e)}")

#         threading.Thread(target=play_speech).start()

#     def display_rec_start(self):
#         """
#         Displays the recording start indicator on the Uno application window.
#         """
#         logging.info("Displaying recording start")
#         self.windowSurface.fill(BACK_COLOR)
#         pygame.draw.circle(self.windowSurface, REC_COLOR, (WIDTH // 2, HEIGHT // 2), REC_SIZE)
#         pygame.display.flip()

# def main():
#     """
#     The main function that initializes and runs the Uno application.
#     """
#     logging.info("Starting Uno")
#     pygame.init()

#     with open(INPUT_CONFIG_PATH, encoding='utf-8') as data:
#         config_yaml = yaml.safe_load(data)
#     config = Config(config_yaml)

#     uno = Uno(config)
#     uno.run()

# if __name__ == "__main__":
#     main()