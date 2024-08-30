from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('upload_image/', views.upload_image, name='upload_image'),
    path('enter_url/', views.enter_url, name='enter_url'),
    path('weather/', views.weather_view, name='weather'),
]
