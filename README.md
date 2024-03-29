# Project 1
## CS490: Guided Design in Software Engineering
This project is to build and deploy a simple “music discovery” web app that shows song(s) from my favorite artist(s) and link(s) to the music and lyrics. The data will be dynamically generated using third-party APIs from Spotify and Genius.

## Spotify API and Python
[The Spotify Web API](https://developer.spotify.com/documentation/web-api/) allows applications to fetch lots of amazing data from the Spotify catalog, as well as manage a user's playlists and saved music. Some examples of information you get are:
* Track, artist, album, and playlist metadata and search.
* High-level audio features for tracks.
* In-depth audio analysis for tracks.
* Featured playlists and new releases.
* Music recommendations based on seed data.

#### To Obtain Authorization:
1. [Register your Application](https://developer.spotify.com/documentation/general/guides/app-settings/#register-your-app)
2. Have your application request refresh and access tokens; Spotify returns access and refresh tokens.
* When the authorization code has been received, you will need to exchange it with an access token by making a POST request to the Spotify Accounts service, this time to its /api/token endpoint: `POST https://accounts.spotify.com/api/token`
* Follow the Refreshable user [Authorization Code Flow](https://developer.spotify.com/documentation/general/guides/authorization-guide/#authorization-code-flow)

## Genius API and Python
[The Genius API](https://docs.genius.com/#/getting-started-h1) allows hosts to fetch bunch of song lyrics and lets users highlight and annotate passages with interpretations, explanations, and references. Examples of information that you can gather from this api includes:
* Searching Songs, Artists and Lyrics. 
* Get Lyrics information for any Artist or Song.

#### Getting Started
1. Start by registering your application by visiting [API Client Management Page](http://genius.com/api-clients) and create an API for your application.
2. Since our app doesn’t require user-specific data, we can use the flow defined in the section “Access for Apps Without Users” in `https://docs.genius.com/#/authentication-h1`

## Install Requirements
1. `pip install python-dotenv`
2. `pip install requests`
3. `pip install -U Flask`

## Setup
1. Create `.env` file in your main directory
2. Add your CLIENT ID and CLIENT SECRET KEY from [Spotify for developers](https://developer.spotify.com/dashboard/) with the lines: `client_id= 'YOUR_ID'` followed by `client_secret='YOUR_SECRET_KEY'`
3. Add your access token from [Genius API](http://genius.com/api-clients) with lines: `access_token= 'YOUR ACCESS TOKEN'`

## Run Application
1. Run command in terminal `python app.py`.
2. See output using the preview tab on cloud9. 
3. Refresh/Reload the page to see random tracks and their artists.
4. Click on the get lyrics box to get the lyrics of that displayed song.
5. On the search tap underneath the Spoti-py logo, enter your personal favorite artist to get the information of a random song from that artist. 

## Technical Problems
What are at least 3 technical issues you encountered with your project? How did you fix them?
* In the beginning of starting the project, I was having authentication issue from spotify. I was not able to fetch any information the the spotify api because of that. To solve this problem
I carefully followed the [Crendentials Flow guide](https://developer.spotify.com/documentation/general/guides/authorization-guide/#client-credentials-flow) and found out that I was using the wrong
api token link for `POST`. Instead of `https://accounts.spotify.com/api/token` I was using `https://accounts.spotify.com/authorize?` which was giving me problems.
* While working on the project and executing it, my `app.py` which is my flask file, was having trouble running as it was displaying an error stating: "No such file or directory". 
To fix this problem I googled this error and found a stack overflow page which recommended me to change the name of my python file which fixed that error.
* Most errors while working on this project I faced were when I was reading and understing the `json()` file generated from the spotify API. Since it was my first time working with API's, I had to 
uderstand the format and structure of the `json()` file. To gather and understand the information from the file well, I googled json formatter and used [JSON formatter and Validator](https://jsonformatter.curiousconcept.com/) tool 
which helped me read the json file clearly.

## Additional Features to be added
Some addiditional feature that I would like to add in my project are:
* A display page of all the top tracks of that artist and not just one.
* I would also like to add a feature where the user can see the reviews of the song being played.

