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
from .forms import StudentForm
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


def add_Student(request):
     if request.method == 'POST':
      student_form = StudentForm(request.POST)  # Use the correct form name
      if student_form.is_valid():
    # Create a new student associated with the user
       student = student_form.save(commit=False)

    # Create a new user
       new_user = User.objects.create_user(username=request.POST['username'])
       new_user.set_password(request.POST['password'])
       new_user.save()

      student.user = new_user
      student.save()

    # Log in the new user
      user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
      if user is not None:
        login(request, user)

      return redirect('home')  # Redirect to home after successful registration


    
    
