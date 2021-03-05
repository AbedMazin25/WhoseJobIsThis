from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.render_page, name='render_page'),
    url(r'^tasks/(?P<task_id>[0-9]+)/$', views.show_info, name='show_info')
]
