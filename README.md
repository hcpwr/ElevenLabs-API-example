# ElevenLabs Speech Recognition

This is a Python console application that listens to your microphone and converts your speech to text. It then plays back the text as audio using the ElevenLabs API.
Installation

    - Clone this repository to your local machine.
    - Install the required dependencies by running pip install -r requirements.txt.
    - Obtain an API key from the ElevenLabs website and replace the API_KEY variable in the main.py file with your key.
    - Replace the VOICE_NAME variable in the main.py file with the name of the voice you want to use.
    - Run the application by executing the main.py file.

# Usage

    - Press the CTRL key to start recording audio.
    - Speak into your microphone.
    - Release the CTRL key to stop recording audio.
    - The application will convert your speech to text and play back the audio using the specified voice.

# Dependencies

    keyboard==0.13.5
    requests==2.26.0
    elevenlabslib==0.0.3
    SpeechRecognition==3.8.1

# Configuration

    API_KEY: Your ElevenLabs API key.
    VOICE_NAME: The name of the voice you want to use.
    BUTTON: Button that will start recording
