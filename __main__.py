import speech_recognition as sr
import requests
import json

def get_llm_response(prompt):
    """
    Sends a prompt to the Ollama API and returns the generated response from the LLM.

    Args:
        prompt (str): The input text to be processed by the LLM.

    Returns:
        str: The generated response from the LLM, or an error message if the request fails.
    """
    url = "http://localhost:11434/api/generate"
    headers = {"Content-Type": "application/json"}
    data = {
        "model": "llama3",
        "prompt": prompt,
        "stream": False
    }
    response = requests.post(url, headers=headers, data=json.dumps(data))
    if response.status_code == 200:
        result = response.json()
        return result["response"]
    else:
        return "Error occurred while generating response."

r = sr.Recognizer()
m = sr.Microphone()

try:
    print("A moment of silence, please...")
    with m as source: r.adjust_for_ambient_noise(source)
    print("Set minimum energy threshold to {}".format(r.energy_threshold))
    while True:
        print("\nSay something!")
        with m as source: audio = r.listen(source)
        print("Got it! Now to recognize it...")
        try:
            # Recognize speech using Google Speech Recognition
            value = r.recognize_google(audio)
            print("\n>>> IN:\n{}".format(value))

            # Send the transcribed text to the LLM
            llm_response = get_llm_response(value)

            # Print the response
            print("\n<<< OUT:\n{}".format(llm_response))

        except sr.UnknownValueError:
            print("Oops! Didn't catch that")
        except sr.RequestError as e:
            print("Uh oh! Couldn't request results from Google Speech Recognition service; {0}".format(e))
except KeyboardInterrupt:
    pass
