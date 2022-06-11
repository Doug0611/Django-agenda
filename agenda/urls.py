from django.urls import path
from . import views

app_name = 'agenda'

urlpatterns = [
    path('', views.home, name='home'),
    path('busca/', views.search, name='search'),
    path('agenda/contato/<int:id_contact>/', views.contact, name='contact')
]
