from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods, require_POST, require_safe

from .models import Movie
from .forms import MovieSearchForm
from critic.models import Oneline, Reply
from critic.forms import OnelineForm, ReplyForm

import tmdbsimple as tmdb
tmdb.API_KEY = '29df6583a904bc9dd4937f055eb9d731'

@require_http_methods(["GET", "POST"])
def detail(request, movie_name, movie_id):
    response = tmdb.Movies(movie_id).info()
    if Movie.objects.filter(title=movie_name).exists():
        movie = get_object_or_404(Movie, title=movie_name)
    else:
        movie = Movie()
        movie.title = response['title']
        movie.poster = response['poster_path']
        movie.released_date = response['release_date']
        movie.running_time = response['runtime']
        movie.tmdb_pk = response['id']
        movie.save()

    oneline_form = OnelineForm()
    reply_form = ReplyForm()

    is_oneline_user = movie.oneline_set.filter(user=request.user).exists()

    return render(request, 'movie/detail.html', {
        'movie': movie,
        'oneline_form': oneline_form,
        'reply_form': reply_form,
        'is_oneline_user': is_oneline_user
    })

@require_safe
def index(request):
    form = MovieSearchForm()
    movies = Movie.objects.order_by('-pk')
    return render(request, 'movie/index.html', {
        'form': form,
        'movies': movies,
    })

@require_http_methods(["GET", "POST"])
def search(request):
    form = MovieSearchForm(request.POST)
    if form.is_valid():
        movie = form.save(commit=False)
        movie_name = movie.title
        search = tmdb.Search()
        response = search.movie(query=movie_name)
        results = []
        for s in search.results:
            results.append([s['title'], s['id']])
        return render(request, 'movie/search.html', {
            'results': results,
        })
