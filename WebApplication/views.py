from django.contrib import messages
from django.shortcuts import render, redirect
from WebApplication.models import User
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def main_view(request):
    return render(request, "main.html")


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = User.objects.get(username=username, password=password)

        if user is not None:

            return render(request, "main.html")
        else:
            return redirect('register')
    return render(request, "login.html")


def logout_user(request):
    logout(request)
    return redirect("login.html")


def register_user(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password = request.POST['password']

        user = User.objects.create(first_name=first_name, last_name=last_name, username=username, password=password)
        user.save()
        messages.success(request, "Your account has been successfully created")

        return redirect('login')

    return render(request, "register.html")
