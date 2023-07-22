from django.urls import path
from animeApp import views

urlpatterns = [
    path('api/animes', views.anime_list),
    path('api/animes/<int:pk>', views.anime_detail),
]

