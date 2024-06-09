
![uno](https://github.com/juanlucasumali/uno/assets/85742113/5961cdf6-b064-4d0f-9b3e-463749dab8ce)

Watch the demo [**here**](https://www.youtube.com/watch?v=eYxorWUVw1g).

# Uno: Voice-Controlled AI Assistant

Uno is a voice-controlled AI assistant that uses the **Ollama** language model and **Whisper** speech recognition to provide an interactive conversational experience. It allows users to communicate with the AI assistant using natural language through speech input and receives responses in both text and speech format.

## Features

- Voice-controlled interaction with the AI assistant
- Real-time speech recognition using the Whisper model
- Text-to-speech output using the pyttsx3 engine
- Integration with the Ollama language model for generating responses
- Customizable configuration through a YAML file
- Push-to-talk functionality for capturing speech input
- Visual indicators for recording status and messages
- Logging for debugging and monitoring purposes

## Requirements

- Python 3.7 or higher
- PyTorch
- Whisper
- pyttsx3
- PyAudio
- Pygame
- requests
- PyYAML

## Installation

1. Install [Ollama](https://ollama.com/).
2. Download the llama model using the `ollama pull llama` command.
3. Download the `base.en` OpenAI Whisper Model [here](https://github.com/openai/whisper/discussions/63#discussioncomment-3798552).
4. Clone and `cd` into the repository:

   ```bash
   git clone https://github.com/your-username/uno.git
   ```
5. Place the downloaded `base.en` Whisper model into a /whisper directory in the repository's root folder.
6. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```
   Or, if you use pip3:
    ```bash
   pip3 install -r requirements.txt
   ```

7. Configure `uno.yaml` in the project directory. Adjust the necessary settings such as API endpoints, model paths, and initial prompts in the YAML file.

## Usage

1. Run the Uno application:

   ```bash
   python main.py
   ```
   Or:
      ```bash
   python3 main.py
   ```

3. The application window will open, and Uno will initialize the necessary components.

4. Press and hold the `Space` key to start recording your speech input.

5. Speak your query or command while holding the `Space` key.

6. Release the `Space` key when you finish speaking.

7. Uno will process your speech input, send it to the Ollama API for generating a response, and then convert the response to speech output.

8. The response will be displayed on the application window and played back as speech.

9. To stop the speech playback, press the `S` key.

10. To exit the application, press the `Esc` key.

## Contributing

Contributions to Uno are welcome! If you find any bugs, have feature requests, or want to contribute improvements, please open an issue or submit a pull request on the GitHub repository.

## Acknowledgements

- [Ollama](https://ollama.com/) - Language model for generating responses
- [Whisper](https://github.com/openai/whisper) - Speech recognition model
- [pyttsx3](https://github.com/nateshmbhat/pyttsx3) - Text-to-speech conversion library
- [PyAudio](https://people.csail.mit.edu/hubert/pyaudio/) - Audio input/output library
- [Pygame](https://www.pygame.org/) - Library for creating graphical user interfaces

## Credits

Uno was heavily inspired by and incorporates code from the following GitHub repositories:

- [ollama-voice-mac](https://github.com/apeatling/ollama-voice-mac) by [Andy Peatling](https://github.com/apeatling) - A voice-controlled AI assistant for macOS using Ollama and Whisper.

I would like to express my gratitude to the authors of these repositories for their valuable contributions and inspiration. 

## Contact

For any questions or inquiries, please contact [juanlucasumali@berkeley.edu](mailto:juanlucasumali@berkeley.edu).

---
