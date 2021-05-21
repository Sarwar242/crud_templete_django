from rest_framework import serializers
from django.utils import timezone
from rest_framework.validators import UniqueValidator
from .models import Subject, Student, gender_choice as CHOICES

class SubSer(serializers.ModelSerializer):
    class Meta:
        model= Subject
        fields= '__all__'


class StuSer(serializers.ModelSerializer):
    class Meta:
        model= Student
        fields= '__all__'
        depth= 2





class StudentSerializer(serializers.ModelSerializer):
    # id = serializers.IntegerField(read_only=True)
    # first_name = serializers.CharField(max_length=200, required=False)
    # last_name  = serializers.CharField(max_length=200, required=False)
    roll       = serializers.CharField(max_length=200,
                                       validators=[UniqueValidator(queryset=Student.objects.all())])
    subject    = SubSer(read_only=True)
    # dob        = serializers.DateField( read_only=True, required=False, default=timezone.now)
    # dob        = serializers.DateField(required=False)
    # gender     = serializers.ChoiceField(choices=CHOICES, default='Male', required=False) 
    # phone      = serializers.CharField( required=False )
    # email      = serializers.EmailField( required=False )
    # image      = serializers.ImageField(required=False )

    class Meta:
        model= Student
        fields= '__all__'

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Student.objects.create(**validated_data)
        