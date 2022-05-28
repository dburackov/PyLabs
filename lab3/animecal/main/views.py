from .forms import RegisterUserForm
from django.shortcuts import render
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
