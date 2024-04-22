import requests
import json
import logging
from typing import Callable

# Constants
OLLAMA_REST_HEADERS = {'Content-Type': 'application/json'}

class LLMManager:
    def __init__(self, config):
        self.config = config
        self.context = []

    def ask_ollama(self, prompt: str, response_callback: Callable[[str], None]):
        """
        Sends a prompt to the Ollama API and returns the generated response from the LLM.

        Args:
            prompt (str): The input text to be processed by the LLM.
            response_callback (Callable[[str], None]): A callback function to handle the generated response.
        """
        logging.info(f"Asking OLLaMa with prompt: {prompt}")
        full_prompt = prompt if hasattr(self, "contextSent") else prompt
        self.contextSent = True
        jsonParam = {
            "model": self.config.ollama.model,
            "stream": True,
            "context": self.context,
            "prompt": full_prompt
        }

        try:
            response = requests.post(self.config.ollama.url, json=jsonParam, headers=OLLAMA_REST_HEADERS,
                                     stream=True, timeout=30)
            response.raise_for_status()

            full_response = ""
            for line in response.iter_lines():
                body = json.loads(line)
                token = body.get('response', '')
                full_response += token

                if 'error' in body:
                    logging.error(f"Error from OLLaMa: {body['error']}")
                    response_callback("Error: " + body['error'])
                    return

                if body.get('done', False) and 'context' in body:
                    self.context = body['context']
                    break

            response_callback(full_response.strip())

        except requests.exceptions.RequestException as e:
            logging.error(f"An error occurred while asking OLLaMa: {str(e)}")
            response_callback("Sorry, an error occurred. Please try again.")