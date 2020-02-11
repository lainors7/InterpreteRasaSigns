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

#{
#  "queryResult":
#    {
#        "queryText": "gratuita", "action": "omu.usuario.plan_suscripcion", "parameters":
#        { "tiposuscripcion": "gratuita" }
#    }
#}