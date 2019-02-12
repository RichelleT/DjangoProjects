from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='Home-Alpha'),
    path('about/', views.about, name='About-Alpha'),
    path('bookone/', views.bookone, name='Alpha-BookOne'),
    path('skyrim/', views.skyrim, name='Alpha-Skyrim'),
    path('oblivion/', views.oblivion, name='Alpha-Oblivion'),
]
