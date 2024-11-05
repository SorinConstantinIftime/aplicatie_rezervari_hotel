from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView, CreateView
from userprofile.forms import NewAccountForm


class UserListView(LoginRequiredMixin, ListView):
    model = User
    template_name = 'registration/user_index.html'


class CreateNewAccount(LoginRequiredMixin, CreateView):
    model = User
    template_name = 'forms.html'
    form_class = NewAccountForm

    def get_success_url(self):
        return reverse('userprofile:lista_utilizatori')
