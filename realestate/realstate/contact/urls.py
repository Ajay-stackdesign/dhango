

from django.contrib import admin
from django.urls import path
from .views import SignupView

urlpatterns = [
    path("signin", SignupView.as_view())
]