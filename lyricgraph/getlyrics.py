import urllib2

from xml.etree.ElementTree import ElementTree
from xml.dom import minidom

import time
import pprint
import re

class GetLyrics(object):
	def __init__(self):
		self.url = "http://api.chartlyrics.com/apiv1.asmx/SearchLyricDirect?artist=%s&song=%s"
		self.pp = pprint.PrettyPrinter(indent=4)

	def fetch(self,artist,song):
		query = self.url % (urllib2.quote(artist),urllib2.quote(song))
		time.sleep(0.01)
		req = urllib2.Request(query)
		req.add_header('User-agent', 'Mozilla/5.0')
		xmldata = urllib2.urlopen(req)
		#tree = ElementTree()
		#tree.parse(xmldata)
		#print tree.findtext('Lyric')
		dom = minidom.parse(xmldata)
		try:
			lyrics = dom.getElementsByTagName("Lyric")[0].firstChild.data
		except:
			print "No Results Found"
			return None
		cleaned_lyrics = " ".join(lyrics.split('\n'))
		c1 = re.sub(r'[.,;:()]',"",cleaned_lyrics)
		c2 = re.sub(r"\s+"," ",c1)
		return c2.lower()
