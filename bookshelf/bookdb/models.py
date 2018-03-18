from django.db import models


class Author(models.Model):
	REGION_CHOICES = (
		('IR','iran'),
		('US','america'),
	)
	name = models.CharField(max_length=20,primary_key = True,unique = True)

class Book(models.Model):
	name = models.CharField(max_length = 50)
	author = models.ForeignKey(Author, on_delete=models.CASCADE , blank=True , null = True)
	edition = models.IntegerField(default = 1)
