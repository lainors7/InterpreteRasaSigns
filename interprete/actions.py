from rasa_sdk import Action
import requests
import json
from datetime import datetime
from connectionWitAI import RecognizeSpeech

import spacy

#nlp = spacy.load('en')
#doc = nlp(u'They are looking for new laptops')

#for token in doc:
#    print(token.text, token.lemma_)

API_URL = "https://h211.eps.ua.es/omuflow"
API_KEY = ""

"""
class SpacyAction(Action):
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

class ApiAction(Action):
	def name(self):
		return "action_animation"

	def run(self, dispatcher, tracker, domain):
		text = RecognizeSpeech('myspeech.wav', 4)
		nlp = spacy.load('es')
		message = text
		doc = nlp(message)

		for token in doc:
			    print(token.text, token.lemma_)
		return  []

"""
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