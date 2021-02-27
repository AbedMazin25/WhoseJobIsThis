from django.shortcuts import render
from .models import Task 

def render_page(request):
	tasks = Task.objects.all().order_by('deadline')
	return render(request, 'taskmanager/index.html', {'tasks' : tasks})


# Create your views here.
