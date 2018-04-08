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
    return render(request, 'narmad.html', context)

def registration(request):
    context = {

    }
    return render(request, 'reg_suc.html', context)

def canteen(request):
    context = {

    }
    return render(request, 'canteen.html', context)

def cart(request):
    context = {

    }
    return render(request, 'cart.html', context)

def council(request):
    context = {

    }
    return render(request, 'council.html', context)