import django.contrib.auth.views
from django.urls import path, include

from . import views, forms

app_name = 'tehtavat'
urlpatterns = [
    path('', views.index, name='index'),
]