from django.urls import path
from . import views

urlpatterns = [
    path('function', views.heeloo),
    path('class', views.helotwo.as_view()), 
    path('reservation', views.home),
]