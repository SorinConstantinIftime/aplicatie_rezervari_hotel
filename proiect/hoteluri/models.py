from django.db import models
from locations.models import Location


class Hoteluri(models.Model):
    stele = (('2_stele', '**'),
             ('3_stele', '***'),
             ('4_stele', '****'))

    nume = models.CharField(max_length=100)
    adresa = models.CharField(max_length=150)
    categorie = models.CharField(max_length=100, choices=stele)
    telefon = models.IntegerField(max_length=10)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.categorie} {self.nume}"

