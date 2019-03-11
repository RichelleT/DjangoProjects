from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='Home-Alpha'),
    path('about/', views.about, name='About-Alpha'),
    path('cv/', views.cv, name='CV-Alpha'),
    path('repo/', views.repo, name='Repo-Alpha'),
]
