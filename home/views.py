from django.shortcuts import render

from rest_framework import viewsets
from .Serializers import *
from .models import *

class EmpViewSet(viewsets.ModelViewSet):
    queryset=Emp.objects.all()
    serializer_class=EmpSerializer
