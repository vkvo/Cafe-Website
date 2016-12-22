from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

# Create your models here.
class Dish(models.Model):
	name = models.CharField(max_length=100)
	description = models.TextField(null=True, blank=True)
	price = models.IntegerField()
	image = models.ImageField(upload_to='images/', default='images/default.jpg')
	
	def __str__(self):
		return self.name
		