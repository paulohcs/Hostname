from django.conf.urls import url

from . import views
from . import models

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^hostname/$', views.hostname, name='hostname'),
    url(r'^create/$', views.create, name='create'),
    url(r'^update/$', views.update, name='update'),
    url(r'^retrieve/$', views.retrieve, name='retrieve'),
    url(r'^list/$', views.list, name='list'),
    #url(r'^action/update$', views.hostnameUpdate, name='actionUpdate'),
    #url(r'^action/create$', views.hostnameCreate, name='actionCreate'),
    url(r'^delete/$', views.delete, name='delete'),
]
