from django.urls import path
from . import views

app_name = 'movie'

urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.search, name='search'),
    path('detail/<str:movie_name>/<int:movie_id>', views.detail, name='detail'),
]
