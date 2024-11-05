from django import forms
from django.contrib.auth.models import User
from django.forms import TextInput
from django.shortcuts import render
from django.contrib.admin.widgets import AdminDateWidget, AdminSplitDateTime


class NewAccountForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username']

        widgets = {
            'first_name': TextInput(attrs={'placeholder': 'Nume', 'class': 'form-control'}),
            'last_name': TextInput(attrs={'placeholder': 'Prenume', 'class': 'form-control'}),
            'email': TextInput(attrs={'placeholder': 'Email', 'class': 'form-control'}),
            'username': TextInput(attrs={'placeholder': 'Username', 'class': 'form-control'}),
        }

    def clean(self):
        field_data = self.cleaned_data
        email_value = field_data.get('email')
        username_value = field_data.get('username')
        if User.objects.filter(email=email_value).exists():
            self._errors['email'] = self.error_class('Emailul deja exista, te rugam adauda un email unic')
        if User.objects.filter(username=email_value).exists():
            self._errors['username'] = self.error_class('Username-ul deja exista')
        return field_data


class DTForm(forms.Form):
    your_name = forms.CharField(max_length=64)
    date_input = forms.DateField(widget=AdminDateWidget())
    date_time_input = forms.DateField(widget=AdminSplitDateTime())


def index(request):
    form = DTForm()
    return render(request, 'index.html', form)
