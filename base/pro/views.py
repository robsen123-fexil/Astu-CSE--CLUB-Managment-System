from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Post
from django.contrib.auth import authenticate
from django.contrib.auth import authenticate , login 
from django.contrib.auth.models import User , auth
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
    if request.method=='POST':
         name=request.POST['name']
         username=request.POST['username']        
         password=request.POST['password']
         confirm_password=request.POST['confirm_password']

         if password == confirm_password:
              if User.objects.filter(username=username).exists():
                messages.info(request, "Username Already Taken")
                return redirect('register')
             
              else:
                  user=User.objects.create_user( username=username,password=password)
                  user.save()
                  return redirect('login_view')
         else:
              messages.info(request, "Password Is Not The Same")
              return redirect('register')
    else:   
        return render(request, 'register.html')
def home(request):
        return render(request, 'home.html')