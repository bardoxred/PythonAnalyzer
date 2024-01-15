from django.urls import path

from .views import main_view, login_view, logout_user, register_user
urlpatterns = [
    path("", main_view, name="main"),
    path("login/", login_view, name="login"),
    path("logout/", logout_user, name="logout"),
    path("register/", register_user, name="register"),
]
