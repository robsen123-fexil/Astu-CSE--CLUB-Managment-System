from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Post, info

from django.contrib.auth import authenticate
from django.contrib.auth import authenticate , login 
from django.contrib.auth.models import User , auth
from django.contrib.auth import authenticate, login
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
                messages.error(request, "Username Already Taken")
                return redirect('registeruser')
            if User.objects.filter(email=email).exists():
                messages.error(request, "Email Is Already In Use")
                return redirect('registeruser')
            else:
                user = User.objects.create_user(username=username, password=password, first_name=first_name , last_name=last_name, email=email)
                user.save()
                users = User.objects.get(username = username, email = email)
                print(users)
                userInfo = info(user = users, sex = "F" )
                userInfo.save()
                return redirect('adminpage')
        else:
            messages.error(request, "Password Is Not The Same")
            return redirect('registeruser')
    else:
        return render(request, 'registeruser.html')



def delete_users(request):
    if request.method == 'POST':
        selected_user_ids = request.POST.getlist('selected_users')

        if selected_user_ids:
            # Exclude 'admin' from the deletion
            selected_user_ids = [id for id in selected_user_ids if id != str(User.objects.get(username='admin').id)]

            # Delete selected users
            User.objects.filter(id__in=selected_user_ids).delete()

            messages.success(request, 'Selected users deleted successfully.')
            return redirect('delete_users')

    # Get a list of all users excluding 'admin'
    user_list = User.objects.exclude(username='admin')

    return render(request, 'deleteuser.html', {'user_list': user_list})
from django.shortcuts import render
from django.contrib.auth.models import User

def user_info(request):
    user_list = User.objects.exclude(username='admin')
   
    
    return render(request, 'user_info.html', {'user_list': user_list})
def add_event(request):
    return render(request, 'add_event.html')
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import update_session_auth_hash
from .forms import CustomPasswordChangeForm  # Import your custom form
from django.shortcuts import render, get_object_or_404

@login_required
def reset_password(request):
    if request.method == 'POST':
        form = CustomPasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Your password was successfully updated!')
            return redirect('home')
        else:
            # Manually handle form errors without raising exceptions
            for field, errors in form.errors.items():
                for error in errors:
                    if 'password' in field:  # Check if the error is related to the password
                        messages.error(request, f"Password error: {error}")
                    # Add more specific checks for other fields if needed

            return redirect('reset_password')
    else:
        form = CustomPasswordChangeForm(request.user)

    return render(request, 'resetpassword.html', {'form': form})


def post_list(request):
    posts = Post.objects.all()
    return render(request, 'postlist.html', {'posts': posts})

from .forms import DeletePostForm

def delete_selected_posts(request):
    if request.method == 'POST':
        form = DeletePostForm(request.POST)
        if form.is_valid():
            selected_posts = form.cleaned_data['selected_posts']
            selected_posts.delete()
            return redirect('post_list')
    else:
        form = DeletePostForm()


    return render(request, 'deletepost.html', {'form': form})
def dashboard(request):
    user_list = User.objects.exclude(username='admin')
   
    
    return render(request, 'dashboard.html', {'user_list': user_list})
# views.py

from django.http import JsonResponse
from django.views.decorators.http import require_POST
from .models import UserProfile
from django.http import JsonResponse

@require_POST
def savedata(request, user_id):
    try:
        user_profile = UserProfile.objects.get(user_id=user_id)
        user_profile.attendance = int(request.POST.get('attendance', 0))
        user_profile.report = request.POST.get('report', '')
        user_profile.contest_score = int(request.POST.get('contest_score', 0))
        user_profile.save()

        return JsonResponse({'status': 'success'})
    except UserProfile.DoesNotExist:
        return JsonResponse({'status': 'error', 'message': 'User not found'})

