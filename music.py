import requests
import os
from dotenv import load_dotenv, find_dotenv
import base64
import random
load_dotenv(find_dotenv())# This is to load your API keys from .env

AUTH_URL="https://accounts.spotify.com/api/token"
Artist1 = "https://api.spotify.com/v1/artists/0Tgdv4JlRUoXWfGTrWgY1m"
Artist2 = "https://api.spotify.com/v1/artists/008PpLcKUtVXle6JSwkq3I"
Artist3 = "https://api.spotify.com/v1/artists/3TVXtAsR1Inumwj472S9r4"
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

response = requests.get(Artist1, headers=headers)
data = response.json()
print("1. "+data['name'])

response = requests.get(Artist2, headers=headers)
data = response.json()
print("2. "+data['name'])

response = requests.get(Artist3, headers=headers)
data = response.json()
print("3. "+data['name'])
print()

response = requests.get(random.choice(Random_artist), headers=headers)
data = response.json()

for i in (data['tracks']):
    print("Song name: " + i['name'])
    print("Song Artist: " + i['album']['artists'][0]['name'])
    print("Song Link: " + i['external_urls']['spotify'])
    print("Song image: " + i['album']['images'][0]['url'])
    print()
