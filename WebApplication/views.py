from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def main_view(request):
    return render(request, "main.html")


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


# return render(request, 'login.html')
