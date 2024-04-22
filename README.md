
[![Uno demo](https://img.youtube.com/vi/eYxorWUVw1g/0.jpg)](https://www.youtube.com/watch?v=eYxorWUVw1g)


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

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/uno.git
   ```

2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Set up the configuration file:

   - Create a file named `uno.yaml` in the project directory.
   - Configure the necessary settings such as API endpoints, model paths, and initial prompts in the YAML file.

## Usage

1. Run the Uno application:

   ```bash
   python uno.py
   ```

2. The application window will open, and Uno will initialize the necessary components.

3. Press and hold the `Space` key to start recording your speech input.

4. Speak your query or command while holding the `Space` key.

5. Release the `Space` key when you finish speaking.

6. Uno will process your speech input, send it to the Ollama API for generating a response, and then convert the response to speech output.

7. The response will be displayed on the application window and played back as speech.

8. To stop the speech playback, press the `S` key.

9. To exit the application, press the `Esc` key.

## Configuration

The `uno.yaml` file allows you to customize various settings for the Uno application. Here are the main configuration options:

- `messages`: Customize the messages displayed on the application window.
- `conversation`: Set the initial prompt for the conversation with the AI assistant.
- `ollama`: Configure the Ollama API endpoint and model settings.
- `whisperRecognition`: Specify the path to the Whisper model and the language for speech recognition.

Please refer to the `uno.yaml` file for more details on each configuration option.

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
