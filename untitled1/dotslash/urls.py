from django.conf.urls import url
from . import views

app_name = 'dotslash'

urlpatterns = [
    url(r'^home/$', views.home, name='home'),
    url(r'narmad/$', views.narmad, name='narmad')
]