from rest_framework import serializers
from api.models import Employees

class EmployeeSerializer(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True)
    class Meta:
        model=Employees
        fields="__all__"