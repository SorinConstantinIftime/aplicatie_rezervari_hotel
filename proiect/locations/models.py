from django.db import models

# Create your models here.
class Location(models.Model):

    hotel = models.CharField(max_length=50)
    camera = models.CharField(max_length=100)
    active = models.BooleanField(default=True)
    creat_la = models.DateTimeField(auto_now_add=True, blank=True)
    actualizat_la = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        return f"{self.hotel} - {self.camera}"