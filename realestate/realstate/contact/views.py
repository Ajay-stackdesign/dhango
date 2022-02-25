# from django.shortcuts import render
#
# # Create your views here.
# from django.contrib.auth import get_user_model
# User = get_user_model()
# from rest_framework.response import Response
# from rest_framework.views import APIView
# from rest_framework import permissions
#
#
# class Signin(APIView):
#     permission_classes = [permissions.AllowAny,]
#
#     def post(self, request, format=None):
#         data = self.request.data
#
#         email = data["email"]
#         name = data["name"]
#         password = data["password"]
#         password2 = data["password2"]
#
#         if password == password2:
#             if User.objects.filter(email=email).exists():
#                 return Response({
#                     "error": "Please Enter the Valid Email"
#                 })
#             else:
#                 if len(password) < 8:
#                     return Response({
#                         "error": "password should be more than 8"
#                     })
#                 else:
#                     user = User.objects.create_user(email=email, password=password, name=name)
#                     user.save()
#                     return Response({
#                         "User Created Successfully"
#                     })
#         else:
#             return Response({"error": "Password do not Match"})
# from django.shortcuts import render

# Create your views here.

from urllib import response
from django.contrib.auth import get_user_model
User = get_user_model()

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions

class SignupView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        data = self.request.data

        name = data['name']
        email = data['email']
        password = data['password']
        password2 = data['password2']

        if password == password2:
            if User.objects.filter(email=email).exists():
                return Response({"error": "Email already exists"})
            else:
                if len(password) < 6:
                    return Response({"error": "Password must be at least 6 characters"})
                else:
                    user = User.objects.create_user(email=email, password=password, name=name)
                    user.save()
                    return Response({"User created SuccessFully!"})
        else:
            return Response({"error": "Password do no match"})



