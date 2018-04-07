from django.shortcuts import render
from django.http import request

# Create your views here.
def home(request):
    context = {

    }
    return render(request, 'home.html', context)

def narmad(request):
    context = {

    }
    return render(request, 'narmad.html', context)