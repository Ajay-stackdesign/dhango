
from dataclasses import fields
from numbers import Real
from rest_framework import serializers
from .models import Realtor

class RealtorSerializers(serializers.ModelSerializer):
    class Meta:
        model = Realtor
        fields = "__all__"