from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.http import Http404, HttpResponse
from django.shortcuts import redirect, render

from .forms import AddTask, RegisterUserForm, SigninWithEmailForm
from .genstr import generate_string
from .models import Task, UserMatch

import datetime

def weblogin(request, email_str):
    auth_list = UserMatch.objects.all()
    current_user = None
    for u in auth_list:
        if u.estring == email_str:
            current_user = u.user
            break

    login(request, current_user)
    messages.success(request,
                     'you are now logged in as {}!'.format(current_user))
    return redirect('taskmanager:render_page')


def weblogout(request):
    logout(request)
    messages.success(request, 'You are logged out of your account!')
    return redirect('taskmanager:render_page')


def registeruser(request):
    registerform = RegisterUserForm(request.POST)

    if registerform.is_valid():
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        username_list = [u.username for u in User.objects.all()]
        email_list = [u.email for u in User.objects.all()]
        if username in username_list:
            messages.success(request,
                             'username {} already exists'.format(username))
            return redirect('taskmanager:render_page')
        if email in email_list:
            messages.success(request, 'email {} already exists'.format(email))
            return redirect('taskmanager:render_page')
        user = User.objects.create_user(username=username,
                                        email=email, password=password)
        messages.success(request, 'Created user {}'.format(user))
        return redirect('taskmanager:render_page')
    return HttpResponse("An error occurred while registering new user!")


def add_task(request):
    if request.method == 'POST':
        addtaskform = AddTask(request.POST)

        if addtaskform.is_valid():
            title = request.POST['title']
            value = request.POST['value']
            estimated_dur = request.POST['estimated_dur']
            deadline = request.POST['deadline']
            date_added = datetime.datetime.now()
            infor = request.POST['infor']
            user = request.user
            Task.objects.create(title=title, value=value, estimated_dur=estimated_dur,
                                deadline=deadline, dateadded=date_added, infor=infor,
                                user=user)
            messages.success(request, 'Added task')
            return redirect('taskmanager:render_page')
        return HttpResponse("an error occurred!")
    is_login = request.user.is_authenticated
    current_user = request.user
    context = {
        'is_login': is_login,
        'current_user': current_user,
    }
    return render(request, 'taskmanager/tasks/add/index.html', context)
    

def signin(request):
    email = "not entered"
    signinform = SigninWithEmailForm(request.POST)
    if signinform.is_valid():
        email = request.POST['email']
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            user = None
        if user is not None:
            auth_list = UserMatch.objects.all()
            str_list = [u.estring for u in auth_list]
            email_str = generate_string()
            while email_str in str_list:
                email_str = generate_string()
            usrmtch = UserMatch(estring=email_str, user=user)
            usrmtch.save()
            message = 'http://localhost:8000/weblogin/{}/'.format(email_str)
            messages.success(request,
                             'Use this link {} and follow \
                              the instructions to login.'
                             .format(message))
        else:
            messages.success(request, 'User does not exist!')
    return redirect('taskmanager:render_page')


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
    is_login = request.user.is_authenticated
    current_user = request.user
    context = {
        'page_obj': page_obj,
        'page_number': page_number,
        'page_count': [str(x+1) for x in range(int(tasks.count() / 3) + 1)],
        'is_login': is_login,
        'current_user': current_user,
    }
    return render(request, 'taskmanager/index.html', context)


def show_info(request, task_id):
    try:
        task = Task.objects.get(id=task_id)
    except Task.DoesNotExist:
        raise Http404("Task Does not exist")
    is_login = request.user.is_authenticated
    current_user = request.user
    context = {
        'task': task,
        'is_login': is_login,
        'current_user': current_user,
    }
    return render(request, 'taskmanager/tasks/index.html', context)

# Create your views here.
