from django.urls import path
from . import views

app_name = 'movie'

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:moviename>/detail/', views.detail, name='detail'),

]
