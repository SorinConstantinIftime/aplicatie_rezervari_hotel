from django.urls import path
from userprofile import views

app_name = 'userprofile'
urlpatterns = [
    path('listare_utilizatori', views.UserListView.as_view(), name='lista_utilizatori'),
    path('adauga_utilizator/', views.CreateNewAccount.as_view(), name='utilizator_nou')
]
