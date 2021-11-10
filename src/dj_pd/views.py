# homepage and login page  
from django.shortcuts import render, redirect
from .forms import LoginForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse

def home_view(request):
    return render(request, 'home.html', {}) # on navbar -> home

def login_view(request):
    error_message = None
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(data=request.POST)  
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user) 
                if request.GET.get('next'):
                    return redirect(request.GET.get('next'))
                else:
                    return redirect('home')    
            else:
                error_message = 'Oops! Something went wrong.'

    return render(request, 'login.html', {'form' : form, 'error_message' : error_message})   

 