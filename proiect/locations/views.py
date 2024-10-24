from django.shortcuts import render
from django.urls import reverse
from django.views.generic import CreateView

from locations.models import Location


class CreateLocationView(CreateView):
    model = Location
    template_name = 'forms.html'
    fields = ['hotel', 'camera']

    def get_success_url(self):
        return reverse('locations:adaugare')