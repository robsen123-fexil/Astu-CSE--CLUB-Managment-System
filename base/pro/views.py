from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Post

from django.contrib.auth import authenticate
from django.contrib.auth import authenticate , login 
from django.contrib.auth.models import User , auth
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import PostForm

#from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        remember_me = request.POST.get('remember_me', False)
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            
            # Check if the user is admin and the password is 'password'
            if username == 'admin' and password == '12345':
                return redirect('adminpage')
            
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password.')

    return render(request, 'login.html')
    
def register(request):
    if request.method=='POST':
         #name=request.POST['name']
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
        return render(request, 'registeruser.html')
def home(request):
        posts=Post.objects.all()
        return render(request, 'home.html',{'posts':posts})
def posts(request, pk):
      posts=Post.objects.get(id=pk)
      return render(request, 'posts.html', {'posts':posts} )      
def adminpage(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirect to the home page after successful submission
    else:
        form = PostForm()

    return render(request, 'adminpage.html', {'form': form})      
def registeruser(request):
    if request.method == 'POST':
        # name = request.POST['name']
        username = request.POST['username']
        password = request.POST['password']
        password2 = request.POST['password2']  # Update this line
        first_name = request.POST['first_name']
        last_name=request.POST['last_name']
        email=request.POST['email']
        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username Already Taken")
                return redirect('registeruser')
            else:
                user = User.objects.create_user(username=username, password=password, first_name=first_name , last_name=last_name, email=email)
                user.save()
                return redirect('adminpage')
        else:
            messages.info(request, "Password Is Not The Same")
            return redirect('registeruser')
    else:
        return render(request, 'registeruser.html')
from django.shortcuts import render
from django.contrib.auth.models import User

def liststudent(request):
    # Get a list of all users
    user_list = User.objects.all()

    # Render the admin page with the list of users
    return render(request, 'liststudent.html', {'user_list': user_list})
# views.py
from django.shortcuts import render, redirect
from django.contrib.auth.models import User

def delete_selected_users(request):
    if request.method == 'POST':
        selected_users = request.POST.getlist('selected_users')

        if selected_users:
            User.objects.filter(id__in=selected_users).delete()

    user_list = User.objects.all()
    return render(request, 'deleteuser.html', {'user_list': user_list})
