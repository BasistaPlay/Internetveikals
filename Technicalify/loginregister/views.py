from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, authenticate, login, logout
from django.contrib.auth import login as auth_login
from .forms import *
from django.contrib import messages


# Create your views here.
def home(request):
    return render(request, 'base/base.html')



def register(request):
    form = CreateUserForm(request.POST)

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            messages.success(request, "Reģistrācija notika veiksmīga")
            return redirect('login')


    context = {'form': form}
    return render(request, 'LoginRegister/Register.html', context)

def login(request):
    if request.method == 'POST':
        list(messages.get_messages(request))
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)
            return redirect('home')
        else:
            messages.warning(request, 'Nav pareizs lietotājvārds vai parole')

    return render(request, 'LoginRegister/Login.html')

def logoutUser(request):
    logout(request)
    return redirect('login')