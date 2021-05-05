from django.shortcuts import render,get_object_or_404
from .models import Subject, Student
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from .forms import SubjectForm,StudentForm
from django.urls import reverse,reverse_lazy  
from django.views.generic.edit import UpdateView, DeleteView
from django.views.generic import ListView, DetailView  
from rest_framework.response import Response
from .serializers import SubSer, StuSer
from rest_framework.decorators import api_view
# Create your views here.
def index(request):
    return render(request, 'index.html')


def app(request):
    students=Student.objects.all()
    return render(request,'app.html',{'students':students})



#Subject
class Addsub(View):
    def get(self, request):
        subs = Subject.objects.all()
        return render(request,'addsub.html', {'subs':subs})
    
    def post(self, request):
        form = SubjectForm(request.POST)
        if form.is_valid():
            new_sub = form.save()
        return HttpResponseRedirect(reverse('addsub'))


class SubDetail(DetailView):
    model = Subject
    template_name = 'editsub.html'


class SubUpdate(UpdateView):
    model = Subject 
    # Use our custom view template to override the default view template.
    template_name = 'editsub.html'    
    # Allow edit fields.
    fields = ['name','short_name','code','status']   
    # Jump link after successfull update.
    success_url = reverse_lazy('addsub')   


class SubDelete(DeleteView):
    model = Subject
    template_name = 'layouts/delete.html'   
    success_url = reverse_lazy('addsub')   



#Students
class Addstudent(View):
    def get(self, request):
        subs = Subject.objects.all()
        return render(request,'addstudent.html', {'subs':subs})
    
    def post(self, request):
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            image_field = form.cleaned_data['image']
            print(image_field)
            new_student = form.save()

        else:
            print(form.errors)
            subs = Subject.objects.all()
            return render(request,'addstudent.html', {'subs':subs, 'errors':form.errors})
            
        return HttpResponseRedirect(reverse('app'))



class StudentUpdate(UpdateView):
    model = Student 
    # Use our custom view template to override the default view template.
    template_name = 'editstudent.html'    
    # Allow edit fields.
    fields = ['first_name','last_name','roll','subject', 'dob', 'gender', 'phone', 'email', 'image']   

    def get_success_url(self):
        return reverse_lazy('student', args=(self.object.id,))


    
class StudentDetail(DetailView):
    model = Student
    template_name = 'editstudent.html'

    def get_context_data(self, **kwargs):
        context = super(StudentDetail, self).get_context_data(**kwargs)
        context['subs'] = Subject.objects.all()
        return context




class StudentDelete(DeleteView):
    model = Student
    template_name = 'layouts/delete_student.html'   
    success_url = reverse_lazy('app')   




@api_view(['GET'])
def subjectList(request):
    subjects= Subject.objects.all()
    serializer= SubSer(subjects, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def subjectJust(request, pk):
    subjects= Subject.objects.get(id=pk)
    serializer= SubSer(subjects, many=False)
    return Response(serializer.data)

@api_view(['GET'])
def studentList(request):
    students= Student.objects.all()
    serializer= StuSer(students, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def studentJust(request, pk):
    students= Student.objects.get(id=pk)
    serializer= StuSer(students, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def studentAdd(request):
    serializer= StuSer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def subjectAdd(request):
    print(request)
    print("*********************************************************************************************")
    serializer= SubSer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def studentUpdate(request,pk):
    student= Student.objects.get(id=pk)
    serializer= StuSer(instance=student, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def subjectUpdate(request,pk):
    subject= Subject.objects.get(id=pk)
    serializer= SubSer(instance=subject, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def studentDelete(request,pk):
    student= Student.objects.get(id=pk)
    student.delete()
    return Response('Deleted')

@api_view(['DELETE'])
def subjectDelete(request,pk):
    subject= Subject.objects.get(id=pk)
    subject.delete()
    return Response('Deleted')