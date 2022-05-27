from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View


def index(request):
    return render(request, 'main/anime.html')


def about(request):
    return render(request, 'main/about.html')



"""""
class MainView(View):
    def get(self, request):
        pass


    def psot(self, request):
        pass


    def 
"""
