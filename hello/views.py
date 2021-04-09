from django.http import HttpResponse
from django.shortcuts import render
from django.utils import timezone

from .models import Post


def hello_django(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'hello/index.html', {'posts':posts})

# Create your views here.
