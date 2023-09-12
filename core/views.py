from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Starters

def home(request):
    starters = Starters.objects.all()
    return render(request, 'index.html', {"starters": starters})

def about(request):
    return render(request, 'about.html')

def event(request):
    return render(request, 'event.html')

def contact(request):
    return render(request, 'contact.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            return redirect("login")
        
    return render(request, 'login.html')


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        repeat_password = request.POST['repeat_password']
        if User.objects.filter(email=email).exists():
            messages.info(request, 'Email is taken')
            return redirect('register')
        elif User.objects.filter(username=username).exists():
            messages.info(request, 'Username is taken')
            return redirect('register')
        elif password != repeat_password:
            messages.info(request, 'Repeat password is not correct')
            return redirect('register')
        else:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save();
            return redirect('login')
    return render(request, 'register.html')
