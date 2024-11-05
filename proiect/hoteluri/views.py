from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views.generic import CreateView, ListView

from hoteluri.forms import HoteluriForm
from hoteluri.models import Hoteluri


class CreateHoteluriView(LoginRequiredMixin, CreateView):
    model = Hoteluri
    form_class = HoteluriForm
    template_name = 'forms.html'

    def get_success_url(self):
        return reverse('hoteluri:lista_hoteluri')


class HoteluriView(LoginRequiredMixin, ListView):
    model = Hoteluri
    template_name = 'hoteluri/hoteluri_index.html'
