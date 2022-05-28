from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from .forms import RegisterUserForm, LoginUserForm
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import View, CreateView


def index(request):
    return render(request, 'main/anime.html')


def about(request):
    return render(request, 'main/about.html')



class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'main/register.html'
    success_url = reverse_lazy('login')

    """""
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Регистрация')
        return dict(list(context.items()) + list(c_def.items()))

    def get_user_context(self):
        """

class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = "main/login.html"

    def get_success_url(self):
        return reverse_lazy('anime_list')


def logout_user(request):
    logout(request)
    return redirect('login')