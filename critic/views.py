from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods, require_POST, require_safe
from django.contrib.auth.decorators import login_required

from .forms import OnelineForm, ReplyForm
from .models import Oneline, Reply

@login_required
@require_POST
def create_oneline(request):
    form = OnelineForm(request.POST)
    if form.is_valid():
        oneline = form.save(commit=False)
        oneline.user = request.user
        oneline.save()
    oneline.user.rated_movie = oneline.movie
    return redirect('movie:detail', oneline.movie.title)

@login_required
@require_http_methods(["GET", "POST"])
def update_oneline(request, oneline_pk):
    oneline = get_object_or_404(Oneline, pk=oneline_pk)
    if request.user != oneline.user:
        return redirect('movie:index')
    if request.method == 'POST':
        form = OnelineForm(request.POST, instance=oneline)
        if form.is_valid():
            oneline = form.save()
            return redirect('movie:detail', oneline.movie.title)
    else:
        form = OnelineForm(instance=oneline)
    return render(request, 'critic/oneline_edit.html', {
        'form': form,
        'oneline': oneline,
    })

@login_required
@require_POST
def delete_oneline(request, oneline_pk):
    oneline = get_object_or_404(Oneline, pk=oneline_pk)
    movie = oneline.movie
    oneline.delete()
    return redirect('movie:detail', movie.title)

@login_required
@require_POST
def create_reply(request, oneline_pk):
    oneline = get_object_or_404(Oneline, pk=oneline_pk)
    form = ReplyForm(request.POST)
    if form.is_valid():
        reply = form.save(commit=False)
        reply.user = request.user
        reply.oneline = oneline
        reply.save()
    return redirect('movie:detail', reply.oneline.movie.title)
    
@login_required
@require_POST
def delete_reply(request, oneline_pk, reply_pk):
    oneline = get_object_or_404(Oneline, pk=oneline_pk)
    reply = get_object_or_404(Reply, pk=reply_pk)
    if request.user != reply.user:
        return redirect('movie:index')
    reply.delete()
    return redirect('movie:detail', oneline.movie.title)

@login_required
@require_POST
def like_oneline(request, oneline_pk):
    oneline = get_object_or_404(Oneline, pk=oneline_pk)
    user = request.user
    if oneline.like_oneline_user.filter(pk=user.pk).exists():
        oneline.like_oneline_user.remove(user)
    else:
        oneline.like_oneline_user.add(user)
    return redirect('movie:detail', oneline.movie.title)




