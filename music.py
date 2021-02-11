import requests
import os
from dotenv import load_dotenv, find_dotenv
import base64
import random
load_dotenv(find_dotenv())# This is to load your API keys from .env

AUTH_URL="https://accounts.spotify.com/api/token"
Random_artist = ["https://api.spotify.com/v1/artists/0Tgdv4JlRUoXWfGTrWgY1m/top-tracks?market=US",
                 "https://api.spotify.com/v1/artists/1mYsTxnqsietFxj1OgoGbG/top-tracks?market=US",
                 "https://api.spotify.com/v1/artists/4YRxDV8wJFPHPTeXepOstw/top-tracks?market=US"]
                 
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

header = {
    "Authorization": f"Bearer {os.getenv('access_token')}" #GENIUS API
}

def get_data():
    response = requests.get(random.choice(Random_artist), headers=headers)
    data = response.json()
    
    rtn_array = []
    
    for i in (data['tracks']):
        song_name = i['name']
        song_link = i['preview_url']
        song_image = i['album']['images'][0]['url']
        song_lyrics = get_lyrics(song_name)
        artist_array = []
        for j in range(len(i['album']['artists'])):
            artist_array.append(i['album']['artists'][j]['name'])
        song_artist = str(artist_array)[1:-1].replace("'", "")
        array = [song_name,song_artist,song_link,song_image,song_lyrics]
        rtn_array.append(array)
    random_artist = [random.choice(rtn_array)]
    random_artist.append(data['tracks'][1]['artists'][0]['name'])
    return random_artist
    
def get_lyrics(name):
    url = f"https://api.genius.com/search?q={name}"
    response = requests.get(url, headers = header)
    try:
        data = response.json()
        lyrics_url = data['response']['hits'][0]['result']['url']
        return lyrics_url
    except:
        try:
            name = name.split('(')
            name = name[0]
            url = f"https://api.genius.com/search?q={name}"
            response = requests.get(url, headers = header)
            data = response.json()
            lyrics_url = data['response']['hits'][0]['result']['url']
            return lyrics_url
        except:
            pass