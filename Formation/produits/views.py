from django.shortcuts import render
from . import views
appname = 'Formation'


def home(request):
    return render(request, 'index.html')