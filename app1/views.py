from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def first(request):
    return HttpResponse('<h1>zain is my crush</h1>')
    
