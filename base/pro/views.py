from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Post
from django.contrib.auth import authenticate
from django.contrib.auth import authenticate , login 

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        remember_me = request.POST.get('remember_me', False)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Login successful!')
            return redirect('home')  
        else:
            messages.error(request, 'Invalid username or password.')

    return render(request, 'login.html')
def register(request):
    return render(request, 'register.html')
def home(request):
        return render(request, 'home.html')
