from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import *


# Create your views here.
@login_required
def index(request):
    pass
