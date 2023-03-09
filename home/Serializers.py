from .models import *
from rest_framework import serializers


class EmpSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        fields='__all__'
        model=Emp