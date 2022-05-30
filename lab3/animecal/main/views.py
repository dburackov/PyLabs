import logging

from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from .forms import RegisterUserForm, LoginUserForm, CommentForm, AnimeForm
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import View, CreateView, ListView, TemplateView, DetailView
from .models import Anime, Comment


logger = logging.getLogger('django')


class AnimeList(ListView):
    model = Anime
    template_name = 'main/anime_list.html'
    context_object_name = 'anime'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get_queryset(self):
        return Anime.objects.order_by('year')


class AboutView(TemplateView):
    template_name = 'main/about.html'


class ContactsView(TemplateView):
    template_name = 'main/contacts.html'


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'main/register.html'
    success_url = reverse_lazy('login')


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = "main/login.html"

    def get_success_url(self):
        return reverse_lazy('anime_list')


class AnimeView(CreateView):
    model = Comment
    template_name = 'main/anime.html'
    form_class = CommentForm

    def get_success_url(self):
        return self.request.path

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.anime_id = Anime.objects.get(pk=self.kwargs['anime_id'])
        obj.author = self.request.user.username
        obj.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['anime'] = Anime.objects.get(pk=self.kwargs['anime_id'])
        context['comments'] = Comment.objects.filter(anime_id=self.kwargs['anime_id'])
        return context


class CreateAnimeView(UserPassesTestMixin, CreateView):
    model = Anime
    template_name = 'main/create.html'
    form_class = AnimeForm

    def test_func(self):
        return self.request.user.is_staff

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class AnonsView(ListView):
    model = Anime
    template_name = 'main/anons.html'
    context_object_name = 'anime'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get_queryset(self):
        return Anime.objects.filter(status='Анонс')


class OngoingView(ListView):
    model = Anime
    template_name = 'main/ongoing.html'
    context_object_name = 'anime'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get_queryset(self):
        return Anime.objects.filter(status='Онгоинг')


def logout_user(request):
    logout(request)
    return redirect('login')