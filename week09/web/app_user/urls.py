from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('password/', views.password, name='password'),
    path('index/', views.index, name='index')
]