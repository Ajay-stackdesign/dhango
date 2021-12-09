# from django.shortcuts import render

# Create your views here.
# from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'index.html', {'titles': 'ajay'})

def profile(request):
    return render(request, "profile.html")

def about(request):
    return render(request, "about.html");

def contact(request):
    return render(request, "contact.html")

def expression(request):
    a=int(request.POST["text1"])
    b=int(request.POST["text2"])
    c=a*b
    return render(request, "output.html", {"result": c})

