

from rest_framework.views import APIView
from rest_framework.response import Response
from django.core.mail import send_mail
from rest_framework import permissions
from .models import Contacts

class ContactCreateView(APIView):
    permission_classes = (permissions.AllowAny, )

    def post(self, request, format=None):
        data= self.request.data


        try:
            send_mail(
                data["subject"],
                'Name: '
                +data['name']
                +'\nEmail: '
                +data["email"]
                +'\n\nMessage: \n'
                +data["message"],
                'sahnijkmr@gmail.com',
                ["sahnijkmr@gmail.com"],
                fail_silently=False
            )

            contact = Contacts(name=data["name"], email=data["email"], subject=data["subject"], message = data["message"])
            contact.save()

            return Response({"success": "Message Send SuccessFully"})

        except: 
            return Response ({
                "erros": "Message failed to send"
            })