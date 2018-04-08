from django.conf.urls import url
from . import views

app_name = 'dotslash'

urlpatterns = [
    url(r'^home/$', views.home, name='home'),
    url(r'narmad/$', views.narmad, name='narmad'),
    url(r'registration/$', views.registration, name='register'),
    url(r'^canteen/$', views.canteen, name='canteen'),
    url(r'^cart/$', views.cart, name='cart'),
    url(r'^council/$', views.council, name='council'),
]