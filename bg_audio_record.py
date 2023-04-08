
import keyboard
import requests

from elevenlabslib import *
import speech_recognition as sr

API_KEY = ""	#Your API key
VOICE_NAME = ""	#Your Voice Name goes there

user = ElevenLabsUser(API_KEY)
voice = user.get_voices_by_name(VOICE_NAME)[0]  # List because more than 1 voices can have same name

def start_bg_watch():
	r = sr.Recognizer()
	with sr.Microphone() as source:
		print("Press CTRL to start recording your mic")
		audio_frames = []
		while True:
			if keyboard.is_pressed('ctrl'):
				audio_frames.append(r.listen(source))
			else:
				if audio_frames:
					audio = r.recognize_google(audio_frames[0])
					for frame in audio_frames[1:]:
						audio += " " + r.recognize_google(frame)
					voice.generate_and_play_audio(audio, playInBackground=False)
					audio_frames.clear()
				else:
					pass

start_bg_watch()