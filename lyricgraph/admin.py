from django.contrib import admin
from lgweb.lyricgraph.models import *

class LyricGraphAdmin(admin.ModelAdmin):
	pass
class LyricGraphComparisonAdmin(admin.ModelAdmin):
	pass

class RankGAdmin(admin.ModelAdmin):
	pass
class RankCAdmin(admin.ModelAdmin):
	pass

admin.site.register(MLyricGraph,LyricGraphAdmin)
admin.site.register(MLyricGraphComparison,LyricGraphComparisonAdmin)
admin.site.register(LyricGRank,RankGAdmin)
admin.site.register(LyricCRank,RankCAdmin)

