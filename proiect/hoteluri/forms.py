from django import forms
from django.forms import TextInput, ChoiceField, ModelChoiceField, Select

from hoteluri.models import Hoteluri
from locations.models import Location


class HoteluriForm(forms.ModelForm):
    class Meta:
        model = Hoteluri
        fields = '__all__'

        widgets = {
            'nume': TextInput(attrs={'placeholder': 'name', 'class': 'form-class'}),
            'adresa': TextInput(attrs={'placeholder': 'adresa', 'class': 'form-class'}),
            'categorie': Select(attrs={'class': 'form-class'}),
            'telefon': TextInput(attrs={'placeholder': 'telefon', 'class': 'form-class'}),
            'location': Select(attrs={'class': 'form-class'}),
        }
    def __init__(self, *args, **kwargs):
        super(HoteluriForm, self).__init__(*args, **kwargs)

    def clean(self):
        telefon_value = self.cleaned_data.get('telefon', 0)
        print(telefon_value)
        if len(str(telefon_value)) != 10:
            self._errors['telefon'] = self.error_class(['Introduceti fix 10 cifre'])
        return self.cleaned_data

