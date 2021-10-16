import django.contrib.auth.views
from django.urls import path, include

from . import views, forms

app_name = 'main'
urlpatterns = [
    path('', views.index, name='index'),
]