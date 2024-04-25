from django.shortcuts import render, redirect
from .models import App
from django.contrib.auth.models import User, auth
from django.contrib import messages


def admin(request):
    if request.method =='POST':
        
       
        app_icon = request.FILES.get('app_icon')
        
        app_name = request.POST.get('app_name')
        app_link = request.POST.get('app_link')
        app_category = request.POST.get('app_category')
        sub_category = request.POST.get('sub_category')
        points = request.POST.get('points')

        fb = App(app_icon=app_icon, app_name=app_name,app_link=app_link,app_category=app_category,sub_category=sub_category,points=points)
        fb.save()
        
        return render(request, 'admin.html')


    a = App.objects.all()
   
    return render(request, 'admin.html')

def signin(request):
    return render(request, 'index.html')

def register(request):
    if request.method == 'POST':
        # Fetch form data
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        # Validate passwords match
        if password1 != password2:
            messages.error(request, 'Passwords do not match')
            return redirect('register')

        # Check if username or email already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already taken')
            return redirect('register')
        elif User.objects.filter(email=email).exists():
            messages.error(request, 'Email already taken')
            return redirect('register')

        # Create new user
        user = User.objects.create_user(
            username=username, password=password1, email=email,
            first_name=first_name, last_name=last_name
        )
        user.save()

        
        messages.success(request, 'Registration successful. Please login.')
        return redirect('login')


   
    return render(request, 'register.html')
    

def login(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
          
            return render(request, 'admin.html')
        else:
            messages.info(request, 'Invalid Credentials')
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')