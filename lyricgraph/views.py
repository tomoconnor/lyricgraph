import time

from django.template import Context, Template, loader, RequestContext
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render_to_response
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from lgweb.lyricgraph.models import *
from lgweb.lyricgraph.colour import Colour
from lgweb.lyricgraph.utils import *
from lgweb.lyricgraph.generator import Generator
from lgweb.settings import MEDIA_URL

def index(request):
	lg = MLyricGraph.objects.order_by('-rank','-pk')
	lgc = MLyricGraphComparison.objects.order_by('-rank','-pk')
	
	return render_to_response('index.html',{'singles':lg,'doubles':lgc,'media_url':MEDIA_URL},context_instance=RequestContext(request))

def vote(request,dir,gc,graph_id):
	if gc == "g":
		x = MLyricGraph.objects.get(id=graph_id)
		if dir == "up":
			x.rank += 1
		else:
			x.rank -= 1
		x.save()
		return HttpResponseRedirect('/?refresh=' + str(int(time.time())))
	else:
		y = MLyricGraphComparison.objects.get(id=graph_id)
		if dir == "up":
			y.rank += 1
		else:
			y.rank -= 1
		y.save()
		return HttpResponseRedirect('/?refresh=' + str(int(time.time())))

	
def generate(request):
	if request.method != 'POST':
		return HttpResponseRedirect('/')
	else:
		try:
			_artist = request.POST['artist']
			_song = request.POST['song']
			lg = MLyricGraph.objects.get(artist = _artist, song = _song)
		except MLyricGraph.DoesNotExist:
			try:
				G = Generator()
				_fp = G.single(_artist,_song)
			except:
				return HttpResponseRedirect('/')
			if _fp is None:
				return HttpResponseRedirect('/')
			_filename = _fp[0]
			_filepath = _fp[1]
			mlg = MLyricGraph(artist=_artist,song=_song,filename=_filename,filepath=_filepath)
			mlg.save()
			return HttpResponseRedirect('/?refresh=' + str(int(time.time())))
		else:
			return HttpResponseRedirect('/')


def compare(request):
	if request.method != "POST":
		return HttpResponseRedirect('/')
	else:
		try:
			_artist1 = request.POST['artist1']	
			_artist2 = request.POST['artist2']	
			_song1 = request.POST['song1']
			_song2 = request.POST['song2']
			lgc = MLyricGraphComparison.objects.get(artist1 = _artist1, song1 = _song1, artist2 = _artist2, song2 = _song2)
		except MLyricGraphComparison.DoesNotExist:
			G = Generator()
			_fp = G.double(_artist1, _song1, _artist2, _song2)
			_filename = _fp[0]
                        _filepath = _fp[1]
			mlgc = MLyricGraphComparison(artist1 = _artist1, song1 = _song1, artist2 = _artist2, song2 = _song2, filename = _filename, filepath = _filepath)
			mlgc.save()
			return HttpResponseRedirect('/?refresh=' + str(int(time.time())))
		else:
			return HttpResponseRedirect('/')

