from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from app.models import Employee
from app.forms import EmployeeRegistrationForm
from django.shortcuts import redirect, render
from .forms import EmployeeRegistrationForm
from django.shortcuts import render
from .models import Employee




# Create your views here.
def home(request):
    return render(request, 'home.html')
def signupPage(request):
    return render(request, 'login.html')
def login(request):
    return render(request, 'signup.html')

def register_employee(request):
    form=EmployeeRegistrationForm()
    return render(request,"signup.html",{
        "form":form,
        "name":"Mercy Lagat",
    })
def register_employee(request):
    if request.method=="POST":
        form=EmployeeRegistrationForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
    else:
        form=EmployeeRegistrationForm()
    return render(request,"signup.html",{"form":form})

def employee_list(request):
    employees=Employee.objects.all()
    return render(request,"employee_list.html",{ "employees":employees})

def employee_profile(request,id):
    employee=Employee.objects.get(id=id)
    return render(request,"employee_profile.html",{"employee":employee})

def edit_employee(request,id):
    employee=Employee.objects.get(id=id)
    if request.method=="POST":
        form=EmployeeRegistrationForm(request.POST,instance=employee)
        if form.is_valid():
             form.save()
             return redirect("employee_profile",id=employee.id)

    else: 
        form=EmployeeRegistrationForm(instance=employee) 
        return render(request,"edit_employee.html",{"form":form})

# To edit employee details
def editemp(request, eFname):
    employee = Employee.objects.get(eFname=eFname)
    return render(request, "editemployee.html", {'employee':employee})
# To create employee
def emp(request):
    if request.method == "POST":

        form = EmployeeRegistrationForm(request.POST)
        if form.is_valid():
            try:
                
                form.save()
                return redirect("/showemp")
            except:
                pass
    else:
        form = EmployeeRegistrationForm()
    return render(request, "addemp.html", {'form':form})

# To show employee details
def showemp(request):
    employees = Employee.objects.all()
    return render(request, "showemp.html", {'employees':employees})
