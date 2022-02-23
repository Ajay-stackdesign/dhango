from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Student
from .serializer import StudentSerializer

@api_view(["GET"])
def home(request):
    student_object = Student.objects.all()
    serializer = StudentSerializer(student_object,many=True)
    return Response({
        "message": "here is your result",
        "payload": serializer.data
    })

@api_view(["POST"])
def post(request):
    data= request.data
    serializer = StudentSerializer(data= request.data)

    if not serializer.is_valid():
        return Response({
            "message": "something is work"
        })


    serializer.save()
    return Response({
        "success": "posted",
        "payload": serializer.data
    })

@api_view(["PUT"])
def update_request(request, id):
    try:
        student_objects = Student.objects.get(id=id)
        serializer = StudentSerializer(student_objects, data=request.data)

        if not serializer.is_valid():
            return Response({
                "message": "error"
            })
        serializer.save()
        return Response({
            "message": "success"
        })
    except Exception as e:
        return Response({
            "message": "Not working"
        })

@api_view(["DELETE"])
def delete(request, id):
    try:
        student_ord = Student.objects.get(id = id)
        student_ord.delete()
        return Response({
            "message": "success"
        })
    except Exception as e:
        return Response({
            "error": "failed"
        })