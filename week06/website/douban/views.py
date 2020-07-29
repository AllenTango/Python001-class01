from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

# Create your views here.
def index(req:HttpRequest):
    return HttpResponse("Hello, Allen!")

def year(req:HttpRequest, year):
    return HttpResponse(year)

def name(req:HttpRequest, **kwargs):
    return HttpResponse(kwargs["name"])