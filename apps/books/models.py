from django.db import models


class Book(models.Model):
	title = models.CharField(max_length=55, unique=True)
	author = models.CharField(max_length=55, blank=True)
	url = models.URLField(unique=True)
	image = models.ImageField(upload_to="img/books", blank=True)
	subject = models.CharField(max_length=55)

	class Meta:
		ordering = ['title']

	def __str__(self):
		return self.title

	def this_subject(self, subject):
		if self.subject == subject:
			return True
		return False


