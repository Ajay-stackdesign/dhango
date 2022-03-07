from rest_framework.generics import ListAPIView, RetrieveAPIView
from .models import Realtor
from rest_framework import permissions
from .serializers import RealtorSerializers



class RealtorListView(ListAPIView):
    permission_classes = (permissions.AllowAny,)
    queryset = Realtor.objects.all()
    serializer_class = RealtorSerializers
    pagination_class = None

class RealtorView(RetrieveAPIView):
    queryset = Realtor.objects.all()
    serializer_class = RealtorSerializers

class ToPsellerView(ListAPIView):
    permission_classes = (permissions.AllowAny, )
    queryset = Realtor.objects.filter(top_Seller = True)
    serializer_class = RealtorSerializers
    pagination_class = None

