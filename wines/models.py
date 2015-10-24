import collections

from django.db import models
from jsonfield import JSONField

# Create your models here.

class Grape(models.Model):

	TYPES_OF_WINES = (
		("red_wine", "Red Wine"),
		("white_wine", "White Wine"),
		("rose_wine", "Rose Wine")
	)
	name = models.CharField(max_length=30)
	type = models.CharField(max_length=30, choices=TYPES_OF_WINES)
	


	def __str__(self):
		return "<Grape: {}>".format(self.name)

class Wine(models.Model):

	
	RATINGS = (
		(1, 1),
		(2, 2),
		(3, 3),
		(4, 4),
		(5, 5)
	)
	vineyard = models.CharField(max_length=50)
	name = models.CharField(max_length=50)
	year = models.IntegerField()
	type = models.ForeignKey(Grape)
	country = models.CharField(max_length=50)

	# this is because Djando doesn't support native JSSON fields for Postgres
	image = JSONField(load_kwargs={'object_pairs_hook': collections.OrderedDict})
	notes = models.TextField()
	rating = models.IntegerField(default=1, choices=RATINGS)

	def __str__(self):
		return "<Wine: {}>".format(self.name)




class User(models.Model):
	stp_id = models.CharField(max_length=200)
	name = models.CharField(max_length=50)
	email = models.CharField(max_length=50)
	wines = models.ManyToManyField(Wine)


	def __str__(self):
		return "<User: {}>".format(self.name)