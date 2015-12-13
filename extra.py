import stagger,os
from stagger.id3 import *
from music.models import Song
list = os.listdir(os.getcwd())
for song in list:
	if song.endswith('.mp3'):
		tag = stagger.read_tag(song)
		name = tag.title.rstrip(' - DJMaza.Info')
		artist = tag.artist
		album = tag.album
		print(name+' '+album+' '+artist)
		Song.objects.create(songName=name,album=album,artist=artist)
