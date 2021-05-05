from rest_framework import serializers
from .models import Subject, Student

class SubSer(serializers.ModelSerializer):
    class Meta:
        model= Subject
        fields= '__all__'

class StuSer(serializers.ModelSerializer):
    class Meta:
        model= Student
        fields= '__all__'
