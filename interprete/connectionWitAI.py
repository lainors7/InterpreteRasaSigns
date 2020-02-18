import requests
import json
from recorder import record_audio, read_audio
 
# Wit API endpoint
API_ENDPOINT = 'https://api.wit.ai/speech'
 
# Wit.ai api access token
wit_access_token = '2FH3WJEUTXTYJ4I4VFZL33RR4ERDYEYJ'

# Numero de segundo que dura la grabacion
num_seconds = 9
 
def RecognizeSpeech(AUDIO_FILENAME, num_seconds):
 
    #leyendo el audio definiendo size y fichero
    record_audio(num_seconds, AUDIO_FILENAME)
 
    #leemos el audio
    audio = read_audio(AUDIO_FILENAME)
 
    # definir el header para el http
    headers = {'authorization': 'Bearer ' + wit_access_token, 
                'Content-Type': 'audio/wav', 
                'Transfer-encoding' : 'chunked'
                }
 
    # hacemos el http post request
    resp = requests.post(API_ENDPOINT, headers = headers, data = audio)
 
    # convertir respuesta a json
    data = json.loads(resp.content)
 
    # recoger el texto
    text = data['_text']
    print(text)
    # devolver texto
    return text
 
if __name__ == "__main__":
    text =  RecognizeSpeech('myspeech.wav', num_seconds)
    print("\nYou said: {}".format(text))