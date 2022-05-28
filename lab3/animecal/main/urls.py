from django.urls import path
from .views import *


urlpatterns = [
    path('', AnimeList.as_view(), name='anime_list'),
    path('about', about, name='about'),
    path('register', RegisterUser.as_view(), name='register'),
    path('login', LoginUser.as_view(), name='login'),
    path('logout', logout_user, name='logout'),
]

