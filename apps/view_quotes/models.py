from django.db import models

# Create your models here.
class Author(models.Model):
	"""docstring for Author"""
	first_name = models.CharField(max_length=25)
	last_name = models.CharField(max_length=50)
	created_at = models.DateTimeField()
	updated_at = models.DateTimeField()
	class Meta:
		db_table = "authors"

class Quote(models.Model):
	"""docstring for Quote"""
	author = models.ForeignKey(Author)
	quote = models.TextField()
	created_at = models.DateTimeField()
	updated_at = models.DateTimeField()
	class Meta:
		db_table = "quotes"