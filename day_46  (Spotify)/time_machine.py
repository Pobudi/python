from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth

SPOTIFY_ID = "88b2a5ee1b804f249f62d86b5486c66d"
SPOTIFY_SECRET = "490d225e21b84ac0842eaffe4da31c36"

date = input("From which date would you like to see top charts? (YYYY-MM-DD) ")
response = requests.get(f"https://www.billboard.com/charts/hot-100/{date}/")
soup = BeautifulSoup(response.text, "html.parser")

all_songs = soup.find_all(name="h3", class_=["c-title a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 lrv-u-font-size-18@tablet lrv-u-font-size-16 u-line-height-125 u-line-height-normal@mobile-max a-truncate-ellipsis u-max-width-330 u-max-width-230@tablet-only", "c-title a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 u-font-size-23@tablet lrv-u-font-size-16 u-line-height-125 u-line-height-normal@mobile-max a-truncate-ellipsis u-max-width-245 u-max-width-230@tablet-only u-letter-spacing-0028@tablet"])
all_artists = soup.find_all(name="span", class_=["c-label a-no-trucate a-font-primary-s lrv-u-font-size-14@mobile-max u-line-height-normal@mobile-max u-letter-spacing-0021 lrv-u-display-block a-truncate-ellipsis-2line u-max-width-330 u-max-width-230@tablet-only", "c-label a-no-trucate a-font-primary-s lrv-u-font-size-14@mobile-max u-line-height-normal@mobile-max u-letter-spacing-0021 lrv-u-display-block a-truncate-ellipsis-2line u-max-width-330 u-max-width-230@tablet-only u-font-size-20@tablet"])

charts = [{"song": all_songs[i].string.strip(), "artist": all_artists[i].string.strip().replace(" Featuring", ",").replace(" +", ",").replace(" With", ",").replace(" &", ",").replace(" X", ",").replace(" x", ",")} for i in range(len(all_songs))]

spotipy_resp = spotipy.Spotify(auth_manager=SpotifyOAuth(
                                                client_id=SPOTIFY_ID,
                                                client_secret=SPOTIFY_SECRET,
                                                scope="playlist-modify-private playlist-read-private user-read-recently-played",
                                                redirect_uri="http://example.com",
                                                show_dialog=True,
                                                cache_path="token.txt",
                                                ))
user_id = spotipy_resp.current_user()["id"]

song_uris = []
for chart in charts:
    search_result = spotipy_resp.search(q=f"{chart['song']} artist: {chart['artist']}", type="track")
    try:
        song_uri = search_result["tracks"]["items"][0]["uri"]
        song_uris.append(song_uri)
    except IndexError:
        print(f"{chart['song']} by {chart['artist']}doesn't exist on Spotify :(")

print(len(song_uris))

all_playlists = [title["name"] for title in spotipy_resp.current_user_playlists()["items"]]
name = f"Top 100 in {date}"
if len(all_songs) and len(all_artists) > 0 and name not in all_playlists:
    playlist = spotipy_resp.user_playlist_create(user=user_id, name=name, public=False, collaborative=False, description="  ")
    spotipy_resp.playlist_add_items(playlist["id"], song_uris)
    print("A new playlist was created!")

#window.mainloop()

