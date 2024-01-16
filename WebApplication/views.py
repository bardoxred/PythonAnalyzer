import uuid
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.utils import timezone

from WebApplication.models import Users
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def main_view(request):
    return render(request, "main.html")


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = Users.objects.get(username=username, password=password)
        except:
            user = None
        print(user.__str__)
        if user is not None:
            login(request, user)
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

        user = Users.objects.create(first_name=first_name, last_name=last_name, username=username, password=password)
        user.save()
        messages.success(request, "Your account has been successfully created")

        return redirect('login')

    return render(request, "register.html")

def check_token(request):
    if request.user.is_authentiacted and request.user.token_expiration > timezone.now():
        request.user.token_expiration = timezone.now() + timezone.timedelta(minutes=10)
        request.user.save()
        return HttpResponse("Użytkownik się zalogował")
    else:
        return HttpResponse("Użytkownik niezalogowany albo token wygasł")


