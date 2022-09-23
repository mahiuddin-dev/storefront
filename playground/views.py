from urllib import request
from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.

def hello(request):
    return render(request,'index.html')
