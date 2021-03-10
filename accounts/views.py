from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User


# Create your views here.

def register(request):
    if request.method == 'POST':
        # get form values
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        password2 = request.POST['password2']
        # check if passwords match
        if password == password2:
            #     check if user exists
            if User.objects.filter(username=username).exists():
                messages.error(request, f'User with name ${username} already exists')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, f'User with email ${email} already exists')
                    return redirect('register')
                else:
                    # looks good. let's register this nigga
                    # the user model has a method create_user that creates a user.
                    user = User.objects.create_user(username=username, email=email, password=password,
                                                    first_name=first_name, last_name=last_name)
                    user.save()
                    messages.success(request, 'Registration successful, you can login now')
                    return redirect('login')
                    # let's log the damn user in automatically
                    # auth.login(request, user)
                    # messages.success('You are now logged in ')

        else:
            messages.error(request, 'passwords do not match')
            return redirect('register')

    else:
        return render(request, 'accounts/register.html')


def login(request):
    if request.method == 'POST':
        # login logic
        username = request.POST['username']
        password = request.POST['password']
        # authenticate user
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            # login user (note the difference between authenticate and login)
            auth.login(request, user)
            messages.success(request, 'Login successful')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid credentials')
            return redirect('login')
    else:
        return render(request, 'accounts/login.html')


def dashboard(request):
    return render(request, 'accounts/dashboard.html')


def logout(request):
    if request.method == 'POST':
        # auth logout
        auth.logout(request)
        messages.success(request, 'Logout successful')
        return  redirect('index')
    else:
        return redirect('index')
