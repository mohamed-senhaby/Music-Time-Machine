import requests
import spotipy
from bs4 import BeautifulSoup
from spotipy.oauth2 import SpotifyOAuth

billboard_url = "https://www.billboard.com/charts/hot-100/"
Client_ID = YOUR_CLIENR_ID
Client_Secret = YOUR_CLIENR_SECRET
redirect_URI = "http://example.com"

user_date = input("What year would you like to visit? Type the date in this format YYYY-MM-DD: ")

response = requests.get(url=f"{billboard_url}/{user_date}/")
billboard_response = response.text

soup = BeautifulSoup(billboard_response, "html.parser")

song_titles = [song.getText().strip() for song in soup.select(selector="li #title-of-a-story")]

spotify_auth = spotipy.oauth2.SpotifyOAuth(client_id=Client_ID,
                                           client_secret=Client_Secret,
                                           redirect_uri=redirect_URI,
                                           scope="playlist-modify-private",
                                           show_dialog=True,
                                           cache_path="token.txt"
                                           )
spotify_auth.get_access_token(as_dict=False)
s = spotipy.Spotify(oauth_manager=spotify_auth)
user_id = s.current_user()["id"]

song_uris = []
year = user_date.split("-")[0]
for song in song_titles:
    result = s.search(q=f"track:{song} year:{year}", type="track")
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

playlist = s.user_playlist_create(user_id, name=f"{user_date} Billboard 100", public=False,
                                  description="Musical Time Machine")

s.playlist_add_items(playlist_id=playlist['id'], items=song_uris)
