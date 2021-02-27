from django.db import models
from django.conf import settings
from hello.models import Post
class Task(models.Model):
	title = models.CharField(max_length=200)
	value = models.IntegerField(default=0)
	estimated_date = models.DateTimeField('estimated completion date')
	deadline = models.DateTimeField('deadline')
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	
	def __str__(self):
		return self.title
	
