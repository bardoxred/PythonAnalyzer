from django.shortcuts import render


# Create your views here.
def main_view(request):
    return render(request, "main.html")


def login_view(request):
    return render(request, "login.html")
