from secret import client_id, client_secret, redirect_uri
import spotipy
from spotipy.oauth2 import SpotifyOAuth

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id=client_id,
        client_secret=client_secret,
        redirect_uri=redirect_uri,
        scope="user-library-read",
        # scope="user-follow-read",
        show_dialog=True,
    )
)
# print(sp.current_user_followed_artists(limit=20, after=None))
# for n in sp.current_user_followed_artists(limit=50, after=None)["artists"]["items"]:
#     print(n["name"])

# print(
#     sp.playlist_items(
#         "https://open.spotify.com/playlist/4x0ZlZpZY7vOYAVaKkd1Fh?si=8761c2a8ff7b49b3"
#     )
# )

# print(sp.current_user_saved_shows())
for n in sp.current_user_saved_shows(limit=2)["items"]:
    print(n["show"]["name"])
    print("    ", type(sp.show_episodes(n["show"]["id"], limit=1)["items"]))
