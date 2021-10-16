import django.contrib.auth.views
from django.urls import path, include

from . import views, forms

app_name = 'vartiot'
urlpatterns = [
    path('', views.index, name='index'),
]