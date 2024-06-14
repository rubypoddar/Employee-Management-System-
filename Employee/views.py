from django.shortcuts import render,redirect
from .models import *
def ShowEmp(request):
    var = AddEmployee.objects.all()
    return render(request,'Show.html',{"var":var})
def AddEmp(request):
    if request.method == "POST":

        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        if (name and email and password):
            Add = AddEmployee(None,name,email,password)
            Add.save()
        return redirect('/Employee/AddEmp')
    return render(request,"AddEmp.html")
def DelEmp(request, id):
    try:
        emp = AddEmployee.objects.get(id=id)
        emp.delete()
    except AddEmployee.DoesNotExist:
        # Handle the case where the employee does not exist
        pass
    return render(request,"Show.html")
def Update(request, id):
    try:
        emp = AddEmployee.objects.get(id=id)
    except AddEmployee.DoesNotExist:
        # Handle the case where the employee does not exist
        pass
    return render(request,"update.html",{"emp":emp})
def Update_Done(request,id):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        if (name and email and password):
            emp = AddEmployee.objects.get(id=id)
            emp.id = id
            emp.Name = name
            emp.Email = email
            emp.PassWord = password
            emp.save()
    return redirect('/Employee/Show/',{"emp":emp})
