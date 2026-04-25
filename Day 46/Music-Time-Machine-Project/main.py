import requests
from bs4 import BeautifulSoup
from ytmusicapi import YTMusic

# takes input and remove hypens
time_raw =  input("Which year do you want to travel to? Type in YYYY-MM-DD format: ")
time_skip= time_raw.replace("-","")


# setup for request
url= "https://www.officialcharts.com/charts/singles-chart/"
headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36"}

response = requests.get(f"{url}{time_skip}/7501/", headers)
content = response.text
soup = BeautifulSoup(content, "html.parser")

# Scraps the second span from
song_names = soup.select(".chart-name span:nth-child(2)")
song_list = [name.getText().strip() for name in song_names]

yt = YTMusic("browser.json")

playlists = yt.get_library_playlists()
print(f"Found {len(playlists)} playlists in your library.")

#  new playlist creation based on existence
new_playlist_name = f"{time_raw} Billboard 100"

playlist_id = None

for lists in playlists:
    if lists['title'] == new_playlist_name:
        playlist_id = lists["playlistId"]
        break

if not playlist_id:
    playlist_id = yt.create_playlist(
        title=new_playlist_name,
        description=f"Top 100 billboard songs associated with {time_raw}"
    )
    print("Playlist created.")
else:
    print("Playlist already exists.")

# creates playlists dataset:
for song in song_list:
    try:
        # first filter to search with
        songs_result = yt.search(song, filter="songs")
        yt.add_playlist_items(playlist_id, [songs_result[0]["videoId"]])
        print(f"Added: {song}")

    except Exception as e:
        print(f"Error with {song}: {e}")
        continue

print("Playlist Updated")

