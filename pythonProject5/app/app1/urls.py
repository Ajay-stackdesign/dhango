

from django.contrib import admin
from django.urls import path
from .views import home, post, update_request, delete

urlpatterns = [
    path("", home),
    path("student", post),
    path("update-student/<id>", update_request),
    path("delete/<id>/", delete)
]