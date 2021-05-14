from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import dotenv_values  # From address and password is held in a .env file in the working directory


CONFIG = dotenv_values(".env")

# Scraping Billboard 100
date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
response = requests.get("https://www.billboard.com/charts/hot-100/" + date)
soup = BeautifulSoup(response.text, 'html.parser')
song_names_spans = soup.find_all("span", class_="chart-element__information__song")
song_list = soup.find_all(name="span", class_="chart-element__information__song")
artist_list = soup.find_all(name="span", class_="chart-element__information__artist")
song_names = [song.getText() for song in song_names_spans]
song_artist_list = []

for i in range(len(song_list)):
    song_artist_list.append((song_list[i].getText().replace("'", "").split("(")[0], artist_list[i].getText()
                             .split("Featuring")[0]))

# Spotify Authentication
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://127.0.0.1:9090 ",
        client_id=CONFIG["SPOTIFY_ID"],
        client_secret=CONFIG["SPOTIFY_KEY"],
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_id = sp.current_user()["id"]

# Searching Spotify for songs by title
song_uris = []
year = date.split("-")[0]
for (song, artist) in song_artist_list:
    result = sp.search(q=f"track:{song} artist:{artist}", type="track")
    # print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{artist} - {song} doesn't exist in Spotify. Skipped.")

# Creating a new private playlist in Spotify
playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
print(playlist)

# Adding songs found into the new playlist
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
