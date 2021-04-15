from django.shortcuts import render,get_object_or_404
from .models import Subject, Student
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from .forms import SubjectForm
from django.urls import reverse,reverse_lazy  
from django.views.generic.edit import UpdateView, DeleteView
from django.views.generic import ListView, DetailView  

# Create your views here.
def index(request):
    return render(request, 'index.html')


def app(request):
    return render(request,'app.html')


class Addsub(View):
    def get(self, request):
        subs = Subject.objects.all()
        return render(request,'addsub.html', {'subs':subs})
    
    def post(self, request):
        print(list(request.POST.items()))
        print(request.POST['name'])
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



def addstudent(request):
    return render(request,'addstudent.html')

