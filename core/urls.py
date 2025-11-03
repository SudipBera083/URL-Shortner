
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.url_shortened, name='home'),
    

    path('api/shorten/', views.shorten_url, name='shorten_url'),
    path('api/generate-qr/', views.generate_qr, name='generate_qr'),
]

