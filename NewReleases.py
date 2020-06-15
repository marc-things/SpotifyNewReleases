import json

with open('albums.json') as f:
    data = json.load(f)

# print(album_items)

print("\nSINGLES/ALBUMS: ")

album_items = (data['albums']['items'])
for key in range(len(album_items)):
    if album_items[key]['album_type'] == 'album':
        print('album: ' + (album_items[key]['name']))
    elif album_items[key]['album_type'] == 'single':
        print("single: " + (album_items[key]['name']))


print("\nARTISTS: ")
for key in range(len(album_items)):
    artists = (album_items[key]['artists'])
    for key in range(len(artists)):
        print(artists[key]['name'])
