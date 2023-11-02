import spotipy
import spotipy.util as util
from spotipy.oauth2 import SpotifyClientCredentials
from time import sleep
import webbrowser
import pyautogui
import pandas as pd
from getpass import getpass

def get_spotify_data():
    # Set up application credentials
    client_id = "fc2dab8e01b14550af609407445cf693"
    client_secret = getpass()

    # Create an instance of the Spotipy class to interact with the Spotify API
    sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id=client_id, client_secret=client_secret))

    # Define a function to get details of a song
    def get_track_details(track_id):
        try:
            track_info = sp.track(track_id)
            audio_features = sp.audio_features(track_id)
            return {
                'Title': track_info['name'],
                'Artist': ', '.join([artist['name'] for artist in track_info['artists']]),
                'Album': track_info['album']['name'],
                'Release Date': track_info['album']['release_date'],
                'Popularity': track_info['popularity'],
                'Duration (s)': track_info['duration_ms'] / 1000,
                'Explicit': track_info['explicit'],
                'Danceability': audio_features[0]['danceability'] * 100,
                'Energy': audio_features[0]['energy'] * 100,
                'Tempo': audio_features[0]['tempo'],
            }
        except Exception as e:
            print(f"Error fetching track details: {e}")
            return None

    # Lists of country codes and playlist_ids
    country_codes = ['ES', 'PT', 'FR', 'IT', 'GB']
    playlist_ids = ['37i9dQZEVXbNFJfN1Vw8d9', '37i9dQZEVXbKyJS56d1pgi', '37i9dQZEVXbIPWwFssbupI', '37i9dQZEVXbIQnj7RRhdSX', '37i9dQZEVXbLnolsZ8PSNw']

    # Create a list to store DataFrames for each country
    dfs_by_country = []

    # Iterate through countries and playlists
    for country_code, playlist_id in zip(country_codes, playlist_ids):
        # Get songs from the playlist
        top_tracks = sp.playlist_tracks(f'spotify:playlist:{playlist_id}', market=country_code)

        # Create a list of song details
        songs_data = []
        for track in top_tracks['items']:
            track_id = track['track']['id']
            if track_id:
                details = get_track_details(track_id)
                if details:
                    details['Country'] = country_code  # Add a 'Country' column
                    songs_data.append(details)

        # Create a DataFrame with song details for the current country
        df_country = pd.DataFrame(songs_data)

        # Add the DataFrame to the list of DataFrames
        dfs_by_country.append(df_country)

    # Combine all DataFrames into one final DataFrame
    final_df = pd.concat(dfs_by_country, ignore_index=True)
    
    return final_df
