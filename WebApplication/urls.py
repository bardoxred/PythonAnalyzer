from django.urls import path

from .views import main_view, login_view, logout_user

urlpatterns = [
    path("", main_view),
    path("login/", login_view, name='login'),
    path('logout/', logout_user, name='logout')
]

