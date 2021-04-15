from django import forms
from .models import  Subject , Student

class SubjectForm(forms.ModelForm):
    name       = forms.CharField(label='Subject Name', max_length=250)
    short_name = forms.CharField(label='Short Name', max_length=30)
    code       = forms.CharField(label='Subject Code', max_length=100, required=False)
    status     = forms.CharField(label='Active', max_length=100, required=False)


    class Meta:
        model = Subject
        fields = ("__all__")