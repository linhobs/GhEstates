from django.shortcuts import render, redirect
from django.contrib import messages


# Create your views here.

def register(request):
    if request.method == 'POST':
        messages.error(request, 'testing error message')
        return redirect('register')
    else:
        return render(request, 'accounts/register.html')


def login(request):
    if request.method == 'POST':
        #     login logic
        messages.error(request, 'testing error message')
        return redirect('login')
    else:
        return render(request, 'accounts/login.html')


def dashboard(request):
    return render(request, 'accounts/dashboard.html')


def logout(request):
    return redirect('index')
