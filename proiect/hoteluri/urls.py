from django.urls import path
from hoteluri import views

app_name = 'hoteluri'

urlpatterns = [
    path('adaugare/', views.CreateHoteluriView.as_view(), name='adaugare_hotel'),
    path('', views.HoteluriView.as_view(), name='lista_hoteluri')
]