from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    return HttpResponse('Hello, world. You’re at the polls index. first view from Django-HttpResponse, Advance Clean')

def index2(request):
    return HttpResponse('Hello index')

"""
def templateIndex(request):
    return render()
"""



