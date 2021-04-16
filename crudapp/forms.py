from django import forms
from .models import Subject, Student



CHOICES=(
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Other', 'Other'),
)

prefers = (
    ('JAVA','JAVA'),
    ('Python','Python'),
    ('Discrete Math','Discrete Math'),
    ('Web Technology','Web Technology'),
    ('Robotics','Robotics'),
    ('Numerical Methods','Numerical Methods'),
    ('Machine Learning','Machine Learning'),
)

class SubjectForm(forms.ModelForm):
    name       = forms.CharField(label='Subject Name', max_length=250)
    short_name = forms.CharField(label='Short Name', max_length=30)
    code       = forms.CharField(label='Subject Code', max_length=100, required=False)
    status     = forms.CharField(label='Active', max_length=100, required=False)


    class Meta:
        model = Subject
        fields = ("__all__")



class StudentForm(forms.ModelForm):
    first_name = forms.CharField(label='First Name', max_length=200, required=False)
    last_name  = forms.CharField(label='Last Name', max_length=200, required=False)
    roll       = forms.CharField(label='Roll', max_length=200, required=False)
    subject    = forms.ModelChoiceField(queryset=Subject.objects.all(),  empty_label="(Select)",  required=False)
    dob        = forms.DateField(label='Date Of Birth', required=False)
    gender     = forms.ChoiceField(label='Gender', choices=CHOICES, widget=forms.RadioSelect) 
    phone      = forms.CharField(label='Phone', required=False )
    email      = forms.EmailField(label='Email', required=False )
    image      = forms.ImageField(label='Image', required=False )
    # prefer     = forms.MultipleChoiceField (
    #                         label ='Prefered Subjects',
    #                         required = False,
    #                         disabled = False,
    #                         initial = [],
    #                         choices = prefers,
    #                         widget = forms.CheckboxSelectMultiple)


    class Meta:
        model = Student
        fields = ("__all__")
        