from django.shortcuts import render
from .forms import RegForm
from django.http import request

# Create your views here.
def home(request):
    context = {

    }
    return render(request, 'home.html', context)

def narmad(request):
    myform = RegForm()
    if request.method == "POST":
        form = RegForm(request.POST)
        if form.is_valid():
            myform = form.cleaned_data

    else:
        form = RegForm()
    context = {
        'form': myform,
    }
    return render(request, 'reg_suc.html', context)

def registration(request):
    myform = RegForm()
    if request.method == "POST":
        form = RegForm(request.POST)
        if form.is_valid():
            myform = form.cleaned_data

    else:
        form = RegForm()
    context = {
        'form': myform,
    }
    return render(request, 'reg_suc.html', context)