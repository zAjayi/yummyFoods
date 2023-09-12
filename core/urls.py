from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('event', views.event, name='event'),
    path('contact', views.contact, name='contact'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register')
]