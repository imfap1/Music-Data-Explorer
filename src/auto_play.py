# shows artist info for a URN or URL

from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import sys
import pprint
import webbrowser
import pyautogui
from time import sleep
import pandas as pd
from getpass import getpass

def search_and_play_song(song_name, artist_name=None):
    # Set up Spotify API credentials (moved outside the function)
    client_id = "e082cfefdce54a4d83816d4d258c139d"
    client_secret = getpass()

    # Configure application credentials
    client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)

    # Create a Spotify API instance
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

    query = song_name
    if artist_name:
        query += f" artist:{artist_name}"
    result = sp.search(query)
    if len(result['tracks']['items']) > 0:
        song_uri = result['tracks']['items'][0]['uri']
        webbrowser.open(song_uri)
        sleep(3)
        pyautogui.press('enter')
    else:
        print(f"Song '{song_name}' by '{artist_name}' not found on Spotify.")

def get_track_details(song_name, artist_name=None):
    # Set up Spotify API credentials (moved outside the function)
    client_id = "e082cfefdce54a4d83816d4d258c139d"
    client_secret = "bf908ebca4ee4bba822e49dc9b84f725"

    # Configure application credentials
    client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)

    # Create a Spotify API instance
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

    # Search for the song
    query = song_name
    if artist_name:
        query += f" artist:{artist_name}"
    result = sp.search(query)
    if len(result['tracks']['items']) == 0:
        print(f"Song '{song_name}' by '{artist_name}' not found on Spotify.")
        return

    # Fetch song details
    track_id = result['tracks']['items'][0]['id']
    track_info = sp.track(track_id)
    audio_features = sp.audio_features(track_id)
    duration_ms = track_info['duration_ms']
    duration_seconds = duration_ms / 1000
    duration_minutes = duration_seconds / 60

    # Display song details
    song_details = {
        'Title': track_info['name'],
        'Artist': ', '.join([artist['name'] for artist in track_info['artists']]),
        'Album': track_info['album']['name'],
        'Release Date': track_info['album']['release_date'],
        'Popularity': track_info['popularity'],
        'Duration (minutes)': duration_minutes,
        'Explicit': track_info['explicit'],
        'Danceability': audio_features[0]['danceability'] * 100,
        'Energy': audio_features[0]['energy'] * 100,
        'Tempo': audio_features[0]['tempo'],
    }

    df = pd.DataFrame([song_details])
    print("Song Details:")
    print(df)

# Usage
song_name = input("Enter the song's name: ").upper()
artist_name = input("Enter the artist's name (optional): ").upper()

search_and_play_song(song_name, artist_name)
get_track_details(song_name, artist_name)
