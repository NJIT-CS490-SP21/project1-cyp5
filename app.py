import os

from flask import Flask, render_template
import music

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

print(music.get_data())


@app.route('/')
def hello_world():
    """ Returns root endpoint HTML """
    
    music_data = music.get_data()
    return render_template(
        "index.html",
        music=music_data,
        length=len(music_data)
    )

app.run(
    host=os.getenv('IP', '0.0.0.0'),
    port=int(os.getenv('PORT', 8080)),
    debug=True
)