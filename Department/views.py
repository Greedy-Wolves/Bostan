from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *

# Create your views here.


class Departments(APIView):
    def get(self, request, format=None):
        departments = Department.objects.all()
        serialized_dps = DepartmentSerializer(departments, many=True)
        return Response(serialized_dps.data)