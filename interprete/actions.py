
from rasa_sdk import Action
import requests
import json
from datetime import datetime
import token


API_URL = "https://h211.eps.ua.es/omuflow"
API_KEY = ""

class ApiAction(Action):
	def name(self):
		return "action_animation"

	def run(self, dispatcher, tracker, domain):
			message = tracker.latest_message.get('text')
			print(message)
			dispatcher.utter_message('Ejecutando la busqueda de animaciones...')
			PARAMS = {"queryResult":
   						 {
        					"queryText": message, "action": "omu.usuario.plan_suscripcion", 
							"parameters": 
								{
								 "tiposuscripcion": message
								}
   							}
						}
			r = requests.post(url=API_URL, json = PARAMS)
			data = r.json()
			dispatcher.utter_message(data['fulfillmentText'])
			return  []

#{
#  "queryResult":
#    {
#        "queryText": "gratuita", "action": "omu.usuario.plan_suscripcion", "parameters":
#        { "tiposuscripcion": "gratuita" }
#    }
#}