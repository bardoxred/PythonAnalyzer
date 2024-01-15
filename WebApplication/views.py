from django.shortcuts import render, redirect
from WebApplication.models import User


# Create your views here.
def main_view(request):
    return render(request, "main.html")


def register(request):
    return render(request, "register.html")


def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("main.html")
        else:
            pass
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

