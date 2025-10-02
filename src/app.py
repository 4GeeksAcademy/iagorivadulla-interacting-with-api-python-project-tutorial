import os
import pandas as pd
import matplotlib.pyplot as plt
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv

# load the .env file variables
load_dotenv(override=True) #only works with override


# Spotify API credentials
client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")

#initialize spotipy
spotify = spotipy.Spotify(
    client_credentials_manager = SpotifyClientCredentials(
        client_id=client_id, client_secret=client_secret))

#search for the big brother

big_brother = 'spotify:artist:4J69yWrKwWJgjv3DKTZcGo'
results = spotify.artist_top_tracks(big_brother)

for i in results['tracks'][:10]:
    print(i['name'])

#let's make a data frame
tracks = []
for track in results["tracks"]:
    tracks.append({
        "name": track["name"],
        "album": track["album"]["name"],
        "artist": ", ".join([i["name"] for i in track["artists"]]),
        "popularity": track["popularity"],
        "duration_ms": track["duration_ms"],
        "id": track["id"]
    })

df = pd.DataFrame(tracks)