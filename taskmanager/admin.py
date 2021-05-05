from django.contrib import admin

from .models import Task, UserMatch

admin.site.register(Task)
admin.site.register(UserMatch)

# Register your models here.
