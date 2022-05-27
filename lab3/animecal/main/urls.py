from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='anime_list'),
    path('about/', views.about, name='about'),

]

