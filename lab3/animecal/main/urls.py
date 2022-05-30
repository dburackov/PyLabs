from django.urls import path
from .views import *


urlpatterns = [
    path('', AnimeList.as_view(), name='anime_list'),
    path('about', AboutView.as_view(), name='about'),
    path('register', RegisterUser.as_view(), name='register'),
    path('login', LoginUser.as_view(), name='login'),
    path('contacts', ContactsView.as_view(), name='contacts'),
    path('anime/<int:anime_id>/', AnimeView.as_view(), name='anime'),
    path('anons', AnonsView.as_view(), name='anons'),
    path('ongoing', OngoingView.as_view(), name='ongoing'),
    path('create', CreateAnimeView.as_view(), name='create'),
    path('logout', logout_user, name='logout'),
]

