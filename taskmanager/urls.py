from django.conf.urls import url
from django.urls import path

from . import views

app_name = 'taskmanager'

urlpatterns = [
    path('', views.render_page, name='render_page'),
    path('tasks/<int:task_id>/', views.show_info, name='show_info'),
    path('signin/', views.signin, name='signin'),
    path('weblogin/<str:email_str>/', views.weblogin, name='weblogin'),
    path('weblogout/', views.weblogout, name='weblogout'),
    path('register/', views.registeruser, name='registeruser'),
]
