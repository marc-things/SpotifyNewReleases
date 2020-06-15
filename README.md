### Developer Note:

This is my first personal project while learning Python. I am in the early 
stages and will work on this as I learn new things in Python. 

### Background:

I'm a Spotify user and love to see what new releases come out every Friday.
Right now, I have to manually open the app, click on Browse, click on New
Releases, and then scroll through the list. 

I would rather get an email with all New Releases every friday, which is what
this project is intended for. 

### End Goal: 
Have a fully automated program which sends me an email every Friday with 
New Releases.  The email will include the album art along with the artist 
name(s) and song/album title.  The album art will be a clickable link 
which opens Spotify. 


### Current Implementation:
- I am currently creating the albums.json file manually. 
- I am learning to work with getting information from dictionaries to display 
them in some kind of list. 
- I can now print singles and albums under the "title" SINGLES/ALBUMS and
follow that up with a list of artists under the title ARTISTS.

example output: 
```
SINGLES/ALBUMS:
single: The Bigger Picture
single: Make It Rain
album: Ungodly Hour

ARTISTS: 
Lil Baby
Pop Smoke
Rowdy Rebel
Chloe x Halle
```

### Future Goals:
- figure out how to get a static token for Spotify API as the one provided in
the test API expires. (maybe use https://spotipy.readthedocs.io/ ?)
- figure out how to send an email automatically using Python.
- figure out how to group artists with their album.  As of today, i am able to 
print the singles/albums list first followed by an artist list. This is troublesome
as I don't know which single/album belongs to which artist. 
- figure out how to group artists if they belong to the same single/album.
- Make the email pretty and provide album art along with artist/song/album.
- Make the album art in the email clickable so it opens Spotify and plays music. 

