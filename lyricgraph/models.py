from django.db import models
class MLyricGraph(models.Model):
	artist = models.CharField(max_length=255)
	song = models.CharField(max_length=255)
	filename = models.CharField(max_length=255)
	filepath = models.CharField(max_length=255)
	rank = models.IntegerField(default=100)
	def __str__(self):
		return self.filename
	def get_rank(self):
		return (self.rank - 100)

class MLyricGraphComparison(models.Model):
	artist1 = models.CharField(max_length=255)
	artist2 = models.CharField(max_length=255)
	song1 = models.CharField(max_length=255)
	song2 = models.CharField(max_length=255)
	filename = models.CharField(max_length=255)
	filepath = models.CharField(max_length=255)
	rank = models.IntegerField(default=100)
	def __str__(self):
		return self.filename
	def get_rank(self):
		return (self.rank - 100)

class LyricGRank(models.Model):
	graph = models.ForeignKey(MLyricGraph)
	rank = models.IntegerField(default=100)
	def __str__(self):
		return str(self.rank)

class LyricCRank(models.Model):
	graph = models.ForeignKey(MLyricGraphComparison)
	rank = models.IntegerField(default=100)
	def __str__(self):
		return str(self.rank)

