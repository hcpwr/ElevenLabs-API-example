import keyboard
import requests
from elevenlabslib import *
import speech_recognition as sr

API_KEY = ""	#API key
VOICE_NAME = ""	#Voice Name
BUTTON = 'ctrl'

user = ElevenLabsUser(API_KEY)
voice = user.get_voices_by_name(VOICE_NAME)[0]

def start_bg_watch():
	recognizer = sr.Recognizer()
	with sr.Microphone() as source:
		audio_frames = []
		print("Press ", BUTTON)
		while True:
			if keyboard.is_pressed(BUTTON):
				audio_frames.append(recognizer.listen(source))
			else:
				if audio_frames:
					audio = ""
					for frame in audio_frames:
						audio += recognizer.recognize_google(frame) + " "
					voice.generate_and_play_audio(audio, playInBackground=False)
					audio_frames.clear()
				else:
					pass

start_bg_watch()