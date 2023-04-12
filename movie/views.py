from django.shortcuts import render, redirect, get_object_or_404

from .models import Movie
from critic.models import Oneline, Reply
from critic.forms import OnelineForm, ReplyForm

def detail(request, moviename):
    movie = get_object_or_404(Movie, title=moviename)
    oneline_form = OnelineForm()
    reply_form = ReplyForm()
    return render(request, 'movie/detail.html', {
        'movie': movie,
        'oneline_form': oneline_form,
        'reply_form': reply_form,
    })

def index(request):
    return render(request, 'movie/index.html')

