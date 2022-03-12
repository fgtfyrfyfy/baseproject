from django.shortcuts import render,redirect

from .forms import StudentForms,EmployeeForms,RegistrationForms
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def index(request):
    return render(request,'index.html')

def student(request):
    form=StudentForms
    if request.method=='POST':
        stud_form=StudentForms(request.POST)
        if stud_form.is_valid():
            stud_form.save()
            return redirect('/student')
    return render(request,'student.html',{'form':form})

def employee(request):
    form=EmployeeForms
    if request.method=='POST':
        stud_form=EmployeeForms(request.POST)
        if stud_form.is_valid():
            stud_form.save()
            return redirect('/employee')
    return render(request,'employee.html',{'form':form})

def register(request):
    form=RegistrationForms
    if request.method=='POST':
        reg_form=RegistrationForms(request.POST)
        if reg_form.is_valid():
            reg_form.save()
            return redirect('/register')
    return render(request,'register.html',{'form':form})