from lgweb.lyricgraph.getlyrics import GetLyrics
import sys,os
import pygraphviz as pgv
import pprint
import math
import time
from lgweb.lyricgraph.colour import Colour
from lgweb.lyricgraph.utils import *
from lgweb.settings import *

class Generator(object):
	def __init__(self):
		pass
	
	def single(self,artist,song):
		Blue = Colour(0,0,255)
		White = Colour(255,255,255)
		words_in_song = {}
		filename = "%s-%s.%s"%(p(artist),p(song),filext())
		Fetcher = GetLyrics()
		lyrics = Fetcher.fetch(artist,song)
		if lyrics is None:
			print "No Results found"
			return	
		lyriclist = lyrics.split(" ")
		G = pgv.AGraph()
		G.edge_attr['dir']='forward'
		G.edge_attr['arrowtype'] = 'normal'
		for index in range(0,len(lyriclist)):
			if lyriclist[index] in words_in_song.keys():
				words_in_song[lyriclist[index]] += 1
			else:
				words_in_song[lyriclist[index]] = 1
			
			G.add_node(lyriclist[index])
			if index+1 < len(lyriclist):
				G.add_edge(lyriclist[index],lyriclist[index+1])
			
			for x in words_in_song.keys():
				scaleFactor = int(math.floor((float(words_in_song[x]) / float(len(words_in_song.keys()))) * 255))
				G.get_node(x).attr['color'] = Blue.colourLerp(White,scaleFactor).toHex()
				G.get_node(x).attr['style'] = "filled"
			
			
		G.layout(prog='dot')
		G.write(MEDIA_ROOT + "/graphs/%s.dot"%filename)
		G.draw(MEDIA_ROOT + "/graphs/%s"%filename)
		#pp = pprint.PrettyPrinter()
		#pp.pprint(words_in_song)
		return (filename, MEDIA_ROOT + "/graphs/%s"%filename)
	
	
	def double(self,artist1,song1,artist2,song2):
		Blue = Colour(0,0,255)
		Red = Colour(255,0,0)
		Magenta = Colour(255,0,255)
		White = Colour(255,255,255)
		words_in_song1 = {}
		words_in_song2 = {}
		filename = "%s-%s--vs--%s-%s.%s"%(p(artist1),p(song1),p(artist2),p(song2),filext())
		if True:
			songOne = GetLyrics()
			songTwo = GetLyrics()
			lyricsOne = songOne.fetch(artist1,song1)
			time.sleep(1)
			lyricsTwo = songTwo.fetch(artist2,song2)
			if (lyricsOne is None) or (lyricsTwo is None):
	                        print "No Results found"
	                        return
			lyricsOne_list = lyricsOne.split(" ")
			lyricsTwo_list = lyricsTwo.split(" ")
			G = pgv.AGraph()
	
			G.edge_attr['dir']='forward'
			G.edge_attr['arrowtype'] = 'normal'
	
			for index in range(0,len(lyricsOne_list)):
				if lyricsOne_list[index] in words_in_song1.keys():
					words_in_song1[lyricsOne_list[index]] += 1
				else:
					words_in_song1[lyricsOne_list[index]] = 1
				
				G.add_node(lyricsOne_list[index])
				if index+1 < len(lyricsOne_list):
					G.add_edge(lyricsOne_list[index],lyricsOne_list[index+1])
			
			for index in range(0,len(lyricsTwo_list)):
				if lyricsTwo_list[index] in words_in_song2.keys():
					words_in_song2[lyricsTwo_list[index]] += 1
				else:
					words_in_song2[lyricsTwo_list[index]] = 1
				
				G.add_node(lyricsTwo_list[index])
				if index+1 < len(lyricsTwo_list):
					G.add_edge(lyricsTwo_list[index],lyricsTwo_list[index+1])
		
			for x in words_in_song1.keys():
				scaleFactor = int(math.floor((float(words_in_song1[x]) / float(len(words_in_song1.keys()))) * 255))
				G.get_node(x).attr['color'] = Blue.colourLerp(White,scaleFactor).toHex()
				G.get_node(x).attr['style'] = "filled"
			for x in words_in_song2.keys():
				scaleFactor = int(math.floor((float(words_in_song2[x]) / float(len(words_in_song2.keys()))) * 255))
				G.get_node(x).attr['color'] = Red.colourLerp(White,scaleFactor).toHex()
				G.get_node(x).attr['style'] = "filled"
				if x in words_in_song1:
					G.get_node(x).attr['color'] = Magenta.colourLerp(White,scaleFactor).toHex()
	
						
				
			G.layout(prog='dot')
			G.write(MEDIA_ROOT + "/graphs/%s.dot"%filename)
			G.draw(MEDIA_ROOT + "/graphs/%s"%filename)
			#pp = pprint.PrettyPrinter()
			#pp.pprint(words_in_song1)
			#pp.pprint(words_in_song2)
			return (filename, MEDIA_ROOT + "/graphs/%s"%filename)
		else:
			return (filename, MEDIA_ROOT + "/graphs/%s"%filename)


