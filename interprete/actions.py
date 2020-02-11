from rasa_sdk import Action
import requests
import json
from datetime import datetime

import spacy

#nlp = spacy.load('en')
#doc = nlp(u'They are looking for new laptops')

#for token in doc:
#    print(token.text, token.lemma_)

API_URL = "https://h211.eps.ua.es/omuflow"
API_KEY = ""

class ApiAction(Action):
	def name(self):
		return "action_animation"

	def run(self, dispatcher, tracker, domain):
		nlp = spacy.load('es')
		message = tracker.latest_message.get('text')
		doc = nlp(message)

		for token in doc:
			    print(token.text, token.lemma_)
		return  []


"""
Peticion a IBM para transcripcion de audio a texto

curl -X POST -u "apikey:05DoXwgmiHLNwSa3wrBjU6UX3dKTu4deJuJZR5OYlLRj" \
--header "Content-Type: audio/flac" \
--data-binary @audio-file.flac \
"https://api.eu-gb.speech-to-text.watson.cloud.ibm.com/instances/3a35a1a8-c066-4079-bd2c-0104a4842cb6/v1/recognize"
"""