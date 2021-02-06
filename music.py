import requests
import os
from dotenv import load_dotenv, find_dotenv
import base64
import random
load_dotenv(find_dotenv())# This is to load your API keys from .env

AUTH_URL="https://accounts.spotify.com/api/token"
Random_artist = ["https://api.spotify.com/v1/artists/0Tgdv4JlRUoXWfGTrWgY1m/top-tracks?market=US",
                 "https://api.spotify.com/v1/artists/008PpLcKUtVXle6JSwkq3I/top-tracks?market=US",
                 "https://api.spotify.com/v1/artists/3TVXtAsR1Inumwj472S9r4/top-tracks?market=US"]
                 
client_creds = f"{os.getenv('client_id')}:{os.getenv('client_secret')}"
client_creds_b64 = base64.b64encode(client_creds.encode())

token_data = {
    "grant_type": "client_credentials"
}

token_headers = {
    "Authorization": f"Basic {client_creds_b64.decode()}" 
}

response=requests.post(AUTH_URL,data=token_data,headers=token_headers)
token_response_data = response.json()

access_token = token_response_data['access_token']
headers = {
    "Authorization" : f"Bearer {access_token}"
}

def get_data():
    response = requests.get(random.choice(Random_artist), headers=headers)
    data = response.json()
    
    rtn_array = []
    
    for i in (data['tracks']):
        song_name = i['name']
        song_link = i['preview_url']
        song_image = i['album']['images'][0]['url']
        artist_array = []
        for j in range(len(i['album']['artists'])):
            artist_array.append(i['album']['artists'][j]['name'])
        song_artist = str(artist_array)[1:-1].replace("'", "")
        array = [song_name,song_artist,song_link,song_image]
        rtn_array.append(array)
    return random.choice(rtn_array)

'''
response = requests.get(test, headers=headers)
data = response.json()
for i in (data['tracks']):
    for e in range(len(i['album']['artists'])):
        print(i['album']['artists'][e]['name'])
'''