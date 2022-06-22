from django.urls import path
from . import views

app_name = 'agenda'

urlpatterns = [
    path('', views.home, name='home'),
    path('busca/', views.search, name='search'),
    path('agenda/contato/<int:id_contact>/', views.contact, name='contact'),
    path('delete/<int:id_contact_delete>/', views.delete, name='delete'),
    path('update/<int:id_contact_update>/', views.update, name='update'),
    path('add/', views.add_contact, name='add'),
]
