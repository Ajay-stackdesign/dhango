from urllib import response
from django.contrib.auth import get_user_model
User = get_user_model

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions

class SigninView(APIView):
    permission_classes = (permissions.AllowAny, )

    def post(self, request, format =None):
        data = self.request.data

        name = data["name"]
        email = data["email"]
        password = data["password"]
        password2 = data["password2"]

        if password == password2:
            if User.objects.filter(email=email).exists():
                return Response({"errors": "Email already exists"})
            else:
                if password < 6 :
                    return Response({"errors": "password should be more than 6 charcaters"})
                else:
                    user = User.objects.create_user(email=email, name= name, password=password)

                    user.save()
                    return Response({
                        "succes": "User Created Successfull"
                    })
        else:
            return Response({"error": "Password do not match"})
