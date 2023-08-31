from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from django.shortcuts import render

def task(request):
    return render(request, 'task.html')
