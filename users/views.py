from django.shortcuts import render , redirect
from django.contrib.auth import authenticate , login , logout
from django.contrib import messages
from .models import Users
from django.contrib.auth.hashers import make_password




def login_users(request):

    if request.user.is_authenticated:
        return redirect('tunes.home')
    
    if request.method == 'POST':
        
        email = request.POST.get('email')
        password = request.POST.get('password')
      
        if(email == '' or password == ''):
            messages.error(request, 'Fields cannot be empty')
            return redirect('users.login')
        
        user = authenticate(request , username=email , password=password)
        if user is not None:
            login(request , user)
            return redirect('tunes.home')
        else:
            messages.error(request, 'Invalid Credentials')
            return redirect('users.login')
    
    else :
        return render(request,'registration/login.html')


def signup_user(request):

    if request.user.is_authenticated:
        return redirect('tunes.home')
    
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password= request.POST.get('confirm_password')

        if(email == '' or password == '' or confirm_password == ''):
            messages.error(request, 'Fields cannot be empty')
            return redirect('users.signup')

        if(password != confirm_password):
            messages.error(request, 'Passwords do not match')
            return redirect('users.signup')
        
        if(Users.objects.filter(email=email).exists()):
            messages.error(request, 'Email already exists')
            return redirect('users.signup')
        
        hashed_password = make_password(password)  # Hash the password
        user = Users(email=email, password=hashed_password)
        user.save()  
        
        messages.success(request, 'Account created successfully')
        return redirect('users.login')
    
    return render(request,'registration/signup.html')


def logout_users(request):
    if request.user.is_authenticated:

        logout(request)
        return redirect('users.login')
    else:
        return redirect('users.login')