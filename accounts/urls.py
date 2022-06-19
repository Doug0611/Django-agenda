from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('', views.login, name='index_login'),
    path('logout/', views.logout, name='logout'),
    path('login/', views.login, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('create_account/', views.create_account, name='create_account'),
]
