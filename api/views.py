from django.shortcuts import render

from api.serializers import EmployeeSerializer
from api.models import Employees


from rest_framework.viewsets import ModelViewSet

class EmployeesView(ModelViewSet):
    serializer_class=EmployeeSerializer
    queryset=Employees.objects.all()
    