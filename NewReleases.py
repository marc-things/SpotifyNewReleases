import json

with open('albums.json') as f:
    data = json.load(f)

# print(album_items)
# print(json.dumps(data, indent=4, sort_keys=True))
# print(json.dumps(data['albums']['items'][key]['artists'], indent=4, sort_keys=True))

print("\nNew Music:\n")

album_items = (data['albums']['items'])
for key in range(len(album_items)):
    if album_items[key]['album_type'] == 'album':
        print('ALBUM: ' + (album_items[key]['name']))
    elif album_items[key]['album_type'] == 'single':
        print("SINGLE: " + (album_items[key]['name']))
    artists = data['albums']['items'][key]['artists']
    for key in range(len(artists)):
        print("by " + artists[key]['name'])
    print()


