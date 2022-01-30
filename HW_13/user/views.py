from django.views import generic
from django.contrib.auth.forms import UserChangeForm
from .forms import UserSignUpForm
from django.urls import reverse_lazy


class UserSignUpView(generic.CreateView):
    form_class = UserSignUpForm
    template_name = 'registration/registration.html'
    success_url = reverse_lazy('login')


class UserEditView(generic.CreateView):
    form_class = UserChangeForm
    template_name = 'profiles/edit_profile.html'
    success_url = reverse_lazy('home')
