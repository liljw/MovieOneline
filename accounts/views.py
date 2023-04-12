from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods, require_safe, require_POST
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, get_user_model
from django.http import HttpResponseBadRequest
from .forms import CustomUserCreationForm

User = get_user_model()

@require_http_methods(['GET', 'POST'])
def signup(request):
    if request.user.is_authenticated:
        return redirect('critic:index')
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('critic:index')
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/form.html', {
        'form': form
    })

@require_http_methods(['GET', 'POST'])
def signin(request):
    if request.user.is_authenticated:
        return redirect('critic:index')
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect(request.GET.get('next') or 'critic:index')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/form.html', {
        'form': form
    })

def signout(request):
    logout(request)
    return redirect('critic:index')

@require_safe
def profile(request, username):
    profile_user = get_object_or_404(User, username=username)
    is_follower = profile_user.follower.filter(pk=request.user.pk).exists()
    return render(request, 'accounts/profile.html', {
        'profile_user': profile_user,
        'is_follower': is_follower,
    })

@require_POST
def follow(request, username):
    profile_user = get_object_or_404(User, username=username)
    user = request.user
    if profile_user == user:
        return HttpResponseBadRequest('자기 자신을 팔로우 할 수 없습니다.')
    if profile_user.follower.filter(pk=user.pk).exists():
        profile_user.follower.remove(user)
    else:
        profile_user.follower.add(user)
    return redirect('accounts:profile', profile_user.username)



