
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.url_shortened, name='home'),
]
