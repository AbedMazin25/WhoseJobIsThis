from django.core.paginator import Paginator
from django.http import Http404
from django.shortcuts import render

from .models import Task


def render_page(request):
    tasks = Task.objects.all().order_by('deadline')
    paginator = Paginator(tasks, 3)
    page_number = request.GET.get('page')
    if page_number is None and 'page number' in request.session:
    	page_number = request.session['page number']
    else:
    	page_number = request.GET.get('page')
    	request.session['page number'] = page_number
    	
    page_obj = paginator.get_page(page_number)
    context = {
    	'page_obj': page_obj,
    	'page_number': page_number,
    	'page_count' : [str(x+1) for x in range(int(tasks.count() / 3) + 1)]
    }
    return render(request, 'taskmanager/mainpage.html', context)


def show_info(request, task_id):
    try:
        task = Task.objects.get(id=task_id)
    except Task.DoesNotExist:
        raise Http404("Task Does not exist")
    context = {
        'task': task
    }
    return render(request, 'taskmanager/tasks/index.html', context)

# Create your views here.
