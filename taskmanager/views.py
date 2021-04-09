from django.core.paginator import Paginator
from django.http import Http404
from django.shortcuts import render

from .models import Task


def render_page(request):
    tasks = Task.objects.all().order_by('deadline')
    paginator = Paginator(tasks, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'taskmanager/mainpage.html', {'page_obj': page_obj})


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
