from django.urls import path

from .views import main_view, login_view

urlpatterns = [path("", main_view), path("login/", login_view)]
