from rasa_sdk import Action
import requests
import pyaudio
import json
from datetime import datetime
from connectionWitAI import RecognizeSpeech
from stream import gen

import spacy

num_seconds = 4

API_URL = "https://h211.eps.ua.es/omuflow"
API_KEY = ""
THRESHOLD = .05
CHUNK_SIZE = 1024
FORMAT = pyaudio.paInt16
RATE = 8000
SHORT_NORMALIZE = (1.0/32768.0)
access_key = '2FH3WJEUTXTYJ4I4VFZL33RR4ERDYEYJ' #Token API Wit.ai

class ApiAction(Action):
	def name(self):
		return "action_animation"

	def run(self, dispatcher, tracker, domain):
		p = pyaudio.PyAudio()
		CHUNK_SIZE = 1024
		stream = p.open(format=FORMAT, channels=1, rate=RATE, input=True, output=True, frames_per_buffer=CHUNK_SIZE)

		headers = {'Authorization': 'Bearer ' + access_key,
				'Content-Type': 'audio/raw; encoding=signed-integer; bits=16;' +
				' rate=8000; endian=little', 'Transfer-Encoding': 'chunked'}
		url = 'https://api.wit.ai/speech'

		foo = requests.post(url, headers=headers, data=gen(p, stream))
		stream.stop_stream()
		stream.close()
		p.terminate()
		data = json.loads(foo.content)
		text = data['_text']

		nlp = spacy.load('es')
		message = text
		doc = nlp(message)

		print(message)

		for token in doc:
				print(token.text, token.lemma_)
		return  []
	'''
	def run(self, dispatcher, tracker, domain):
		text = RecognizeSpeech('myspeech.wav', 4)
		nlp = spacy.load('es')
		message = text
		doc = nlp(message)

		print(message)

		for token in doc:
			    print(token.text, token.lemma_)
		return  []
		'''


class DefaultAction(Action):
	def name(self):
		return "action_default_fallback"

	def run(self, dispatcher, tracker, domain):
		dispatcher.utter_message('Lo siento, no te he entendido')
		return  []

"""
Peticion a la api Wit.ai
  curl \
 -H 'Authorization: Bearer 2FH3WJEUTXTYJ4I4VFZL33RR4ERDYEYJ' \
 'https://api.wit.ai/message?v=20200211&q='

	curl -XPOST 'https://api.wit.ai/speech?v=20170307' \
	-i -L \
	-H "Authorization: Bearer 2FH3WJEUTXTYJ4I4VFZL33RR4ERDYEYJ" \
	-H "Content-Type: audio/mpeg3" \
	-H "Transfer-encoding: chunked" \
	--data-binary "@tusaa.mp3"
"""