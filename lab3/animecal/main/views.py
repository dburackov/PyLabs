from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from .forms import RegisterUserForm, LoginUserForm
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import View, CreateView, ListView, TemplateView
from .models import Anime, Comment


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


def show_post(request, anime_id):
    anime = get_object_or_404(Anime, pk=anime_id)
    comments = Comment.objects.filter(anime_id=anime.pk)

    context = {
        'anime': anime,
        'comments': comments,
    }

    return render(request, 'main/anime.html', context=context)


def logout_user(request):
    logout(request)
    return redirect('login')