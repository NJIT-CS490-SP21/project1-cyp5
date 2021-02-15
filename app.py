import os
from flask import Flask, render_template, request
import music
import random

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
Random_artist = ["https://api.spotify.com/v1/artists/1URnnhqYAYcrqrcwql10ft/top-tracks?market=US",
                 "https://api.spotify.com/v1/artists/1mYsTxnqsietFxj1OgoGbG/top-tracks?market=US",
                 "https://api.spotify.com/v1/artists/4YRxDV8wJFPHPTeXepOstw/top-tracks?market=US"]

@app.route('/', methods =["GET", "POST"])
def hello_world():
    """ Returns root endpoint HTML """
    
    if request.method == "POST": 
        artist_name = request.form.get("aname")
        
        try:
            artist_id = music.search(artist_name)
            music_data = music.get_data(artist_id)
            return render_template(
                "index.html",
                music=music_data,
                length=len(music_data[0]),
                )
        except:
            music_data = music.get_data(random.choice(Random_artist))
            return render_template(
                "index.html",
                music=music_data,
                length=len(music_data[0]),
                error_msg = "Artist not Found!!"
            )
    else:
        music_data = music.get_data(random.choice(Random_artist))
        return render_template(
            "index.html",
            music=music_data,
            length=len(music_data[0]),
            )
    
app.run(
    host=os.getenv('IP', '0.0.0.0'),
    port=int(os.getenv('PORT', 8080)),
    debug=True
)