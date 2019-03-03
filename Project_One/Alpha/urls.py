from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='Home-Alpha'),
    path('about/', views.about, name='About-Alpha'),
]
