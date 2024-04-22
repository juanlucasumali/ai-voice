import numpy as np
import pyaudio
import pygame
import pyttsx3
import whisper
import threading
import torch
import queue
import logging

# Constants
INPUT_FORMAT = pyaudio.paInt16
INPUT_CHANNELS = 1
INPUT_RATE = 16000
INPUT_CHUNK = 1024
OLLAMA_REST_HEADERS = {'Content-Type': 'application/json'}
INPUT_CONFIG_PATH = "uno.yaml"

class AudioManager:
    def __init__(self, config):
        self.config = config
        self.audio = pyaudio.PyAudio()
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', self.engine.getProperty('rate'))
        self.model = whisper.load_model(self.config.whisperRecognition.modelPath)

    def waveform_from_mic(self, key=pygame.K_SPACE) -> np.ndarray:
        """
        Captures audio waveform from the microphone while the specified key is pressed.

        Args:
            key (int): The key code of the key to be pressed for audio capture (default: pygame.K_SPACE).

        Returns:
            np.ndarray: The captured audio waveform as a numpy array.
        """

        stream = self.audio.open(format=INPUT_FORMAT, channels=INPUT_CHANNELS, rate=INPUT_RATE,
                                 input=True, frames_per_buffer=INPUT_CHUNK)
        frames = []

        while pygame.key.get_pressed()[key]:
            pygame.event.pump()
            frames.append(stream.read(INPUT_CHUNK))

        stream.stop_stream()
        stream.close()

        return np.frombuffer(b''.join(frames), np.int16).astype(np.float32) * (1 / 32768.0)

    def speech_to_text(self, waveform: np.ndarray) -> str:
        """
        Converts speech audio waveform to text using the Whisper model.

        Args:
            waveform (np.ndarray): The audio waveform to be transcribed.

        Returns:
            str: The transcribed text from the audio waveform.
        """
        logging.info("Converting speech to text")
        result_queue = queue.Queue()

        def transcribe_speech():
            try:
                logging.info("Starting transcription")
                transcript = self.model.transcribe(waveform, language=self.config.whisperRecognition.lang,
                                                   fp16=torch.cuda.is_available())
                logging.info("Transcription completed")
                text = transcript["text"]
                print('\nYOU:\n', text.strip())
                result_queue.put(text)
            except Exception as e:
                logging.error(f"An error occurred during transcription: {str(e)}")
                result_queue.put("")

        threading.Thread(target=transcribe_speech).start()
        return result_queue.get()

    def text_to_speech(self, text: str):
        """
        Converts text to speech using the pyttsx3 engine.

        Args:
            text (str): The text to be converted to speech.
        """
        logging.info(f"Converting text to speech: {text}")
        print('\nUNO:\n', text.strip())

        def play_speech():
            try:
                logging.info("Converting text to speech")
                self.engine.say(text)
                self.engine.runAndWait()
                logging.info("Speech playback completed")
            except Exception as e:
                logging.error(f"An error occurred during speech playback: {str(e)}")

        threading.Thread(target=play_speech).start()

    def stop_speech(self):
        """
        Stops the current speech playback.
        """
        logging.info("Stopping speech")
        self.engine.stop()
        logging.info("Stopped speech")