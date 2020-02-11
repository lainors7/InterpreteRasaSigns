import requests
import json
from recorder import record_audio, read_audio
 
# Wit speech API endpoint
API_ENDPOINT = 'https://api.wit.ai/speech'
 
# Wit.ai api access token
wit_access_token = '2FH3WJEUTXTYJ4I4VFZL33RR4ERDYEYJ'

# Numero de segundo que dura la grabacion
num_seconds = 7
 
def RecognizeSpeech(AUDIO_FILENAME, num_seconds):
 
    # record audio of specified length in specified audio file
    record_audio(num_seconds, AUDIO_FILENAME)
 
    # reading audio
    audio = read_audio(AUDIO_FILENAME)
 
    # defining headers for HTTP request
    headers = {'authorization': 'Bearer ' + wit_access_token, 'Content-Type': 'audio/wav'}
 
    # making an HTTP post request
    resp = requests.post(API_ENDPOINT, headers = headers, data = audio)
 
    # converting response content to JSON format
    data = json.loads(resp.content)
 
    # get text from data
    text = data['_text']
 
    # return the text
    return text
 
if __name__ == "__main__":
    text =  RecognizeSpeech('myspeech.wav', 4)
    print("\nYou said: {}".format(text))