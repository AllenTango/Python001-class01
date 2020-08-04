import json
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from .models import Shorts

# Create your views here.


def index(req: HttpRequest):
    movie = Shorts.objects.all()[0]
    ctx = {
        'name': movie.name,
        'types': movie.type,
        'show_time': movie.show_time,
        'commits': json.loads(movie.commits)
    }
    return render(req, 'index.html', context=ctx)
