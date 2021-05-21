from django.db import models
from django.conf import settings
from phonenumber_field.modelfields import PhoneNumberField
import os
from uuid import uuid4
from django.utils.deconstruct import deconstructible


@deconstructible
class UploadToPathAndRename(object):
    def __init__(self, path):
        self.sub_path = path
               
    def __call__(self, instance, filename):
        ext=filename.split('.')[-1]
        filename='{}.{}'.format(uuid4().hex, ext)
        return os.path.join(self.sub_path, filename)


gender_choice = (
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Other', 'Other'),
)


class Subject(models.Model):
    name       = models.CharField(max_length=250, blank=True)
    short_name = models.CharField( max_length=30, blank=True)
    code       = models.CharField(max_length=100, blank=True)
    status     = models.CharField(max_length=100, blank=True)


    def __str__(self):
        return self.short_name



class Student(models.Model):
    user       = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    first_name = models.CharField(max_length=200, blank=True)
    last_name  = models.CharField(max_length=200, blank=True)
    roll       = models.CharField(max_length=200, blank=True)
    subject    = models.ForeignKey(Subject, on_delete=models.CASCADE, blank=True, null=True)
    dob        = models.DateField(auto_now=False, blank=True, null=True)
    gender     = models.CharField(max_length=50, choices=gender_choice, default='Male')
    phone      = PhoneNumberField(blank=True,null=True)
    email      = models.EmailField(max_length=200,blank=True,null=True)
    image      = models.ImageField(upload_to=UploadToPathAndRename(os.path.join('images','profile_image')), blank=True, null=True)
    # prefer     = models.JSONField(blank=True,null=True)


    def __str__(self):
        return self.first_name+' '+self.last_name


    def delete(self):
        if self.image:
            os.remove(self.image.path)
        return super(Student,self).delete()
