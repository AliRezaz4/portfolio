from urllib import request
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.


def landing_page(request):
    return render(request , "home/test1.html")
