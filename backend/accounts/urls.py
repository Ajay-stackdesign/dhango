from django.contrib import admin

from django.urls import path
from .views import SigninView

urlpatterns = [
    path("signup", SigninView.as_view())
]
