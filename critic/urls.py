from django.urls import path
from . import views

app_name = 'critic'

urlpatterns = [
    path('<str:movie_name>/create/', views.create_oneline, name='create_oneline'),
    path('<int:oneline_pk>/update/', views.update_oneline, name='update_oneline'),
    path('<int:oneline_pk>/delete/', views.delete_oneline, name='delete_oneline'),
    path('<int:oneline_pk>/replies/create/', views.create_reply, name='create_reply'),
    path('<int:oneline_pk>/replies/<int:reply_pk>/delete/', views.delete_reply, name='delete_reply'),
    path('<int:oneline_pk>/like_oneline/', views.like_oneline, name='like_oneline'),
]
