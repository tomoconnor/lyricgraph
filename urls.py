from django.conf.urls.defaults import *
from lgweb.lyricgraph.models import *
from lgweb.lyricgraph.views import *


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^lgweb/', include('lgweb.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
	(r'^admin/', include(admin.site.urls)),
	(r'^$', 'lgweb.lyricgraph.views.index'),
	(r'generate/?','lgweb.lyricgraph.views.generate'),
	(r'compare/?','lgweb.lyricgraph.views.compare'),
	(r'vote_(?P<dir>(up|down))/(?P<gc>([gc]))/(?P<graph_id>(\d+))','lgweb.lyricgraph.views.vote'),

	
)
#(?P<user_name>(\w+))
