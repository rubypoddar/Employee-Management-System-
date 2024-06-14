from django.shortcuts import render
from Employee.views import AddEmp
def Home(request):
    return render(request,"index.html")
def Contact(request):
    return render(request,"contact.html")

def About(request):
    return render(request,"About.html")
