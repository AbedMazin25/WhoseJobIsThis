from django.conf import settings
from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=200)
    value = models.IntegerField(default=0)
    estimated_dur = models.IntegerField(default=1)
    deadline = models.DateTimeField('deadline')
    dateadded = models.DateTimeField('date_added')
    infor = models.TextField(default='no more info')
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class UserMatch(models.Model):
    estring = models.CharField(max_length=20)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE)
