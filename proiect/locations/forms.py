from django import forms
from django.forms import TextInput
from locations.models import Location


class LocationsForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = ['hotel', 'camera', 'pret']

        widgets = {
            'hotel': TextInput(attrs={'class': 'form-control', 'placeholder': 'hotel'}),
            'camera': TextInput(attrs={'class': 'form-control', 'placeholder': 'camera'}),
            'pret': TextInput(attrs={'class': 'form-control', 'placeholder': 'pret'})
        }

    def __init__(self, pk, *args, **kwargs):
        super(LocationsForm, self).__init__(*args, **kwargs)
        self.pk = pk

    def clean(self):
        cleaned_data = super().clean()
        hotel = cleaned_data.get('hotel')
        numar_camera = cleaned_data.get('camera')
        existing_location = Location.objects.filter(hotel=hotel, camera=numar_camera).first()

        if existing_location:
            self._errors['camera'] = self.error_class(['Camera hotelului deja exista'])

        return cleaned_data
