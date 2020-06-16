import spotipy
import spotipy.util as util
from json.decoder import JSONDecodeError
import os
import sys

username = sys.argv[1]
scope = 'user-read-private user-read-playback-state user-modify-playback-state'

# Erase cache and prompt for user permission
try:
    token = util.prompt_for_user_token(username, scope) # add scope
except (AttributeError, JSONDecodeError):
    os.remove(f".cache-{username}")
    token = util.prompt_for_user_token(username, scope) # add scope

spotifyObject = spotipy.Spotify(auth=token)

data = spotifyObject.new_releases(country='US', limit=30)

email_file = open('new_releases.txt', 'w')
email_file.write("New Music:" + '\n\n')
# parsing through json to get singles/albums and their artist names
album_items = (data['albums']['items'])
for key in range(len(album_items)):
    if album_items[key]['album_type'] == 'album':
        email_file.write('ALBUM: ' + (album_items[key]['name'] + '\n'))
    elif album_items[key]['album_type'] == 'single':
        email_file.write("SINGLE: " + (album_items[key]['name'] + '\n'))
    artists = data['albums']['items'][key]['artists']
    for i in range(len(artists)):
        email_file.write("by " + artists[i]['name'] + '\n')
    email_file.write('\n')
email_file.close()
