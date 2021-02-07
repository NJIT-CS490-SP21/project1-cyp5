# Project 1 Milestone 1
## CS490: Guided Design in Software Engineering
This project is to build and deploy a simple “music discovery” web app that shows song(s) from my favorite artist(s) and link(s) to the music and lyrics. The data will be dynamically generated using third-party APIs from Spotify and Genius.

## Spotify API and Python
[The Spotify Web API](https://developer.spotify.com/documentation/web-api/) allows applications to fetch lots of amazing data from the Spotify catalog, as well as manage a user's playlists and saved music. Some examples of of info you get are:
* Track, artist, album, and playlist metadata and search.
* High-level audio features for tracks.
* In-depth audio analysis for tracks.
* Featured playlists and new releases.
* Music recommendations based on seed data.

## Install Requirements
1. `pip install python-dotenv`
2. `pip install requests`

## Setup
1. Create `.env` file in your main directory
2. Add your CLIENT ID AND CLIENT SECRET KEY from [Spotify for developers](https://developer.spotify.com/dashboard/) with the line: `client_id= 'YOUR ID'` and `client_secret='YOUR SECRET KEY'``

