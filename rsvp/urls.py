from django.urls import path
from . import views

urlpatterns = [
    path('', views.startseite, name='start'),
    path('index/', views.index, name='index'),
    path('confirmation/', views.confirmation, name='confirmation'),
    path('guest_summary/', views.guest_summary, name='guest_summary'),
]

