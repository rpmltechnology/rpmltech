from django.shortcuts import render
from . import models
from . import forms
# Create your views here.
def home(request):
    head=models.Header.objects.all()
    form_class= forms.ContactusForm
    return render(request,"app/index.html",{"head":head,'form':form_class})

def it_outsourcing(request):
    head=models.Header.objects.all()
    return render(request,"app/it_outsourcing.html",{"head":head})
def ims(request):
    head=models.Header.objects.all()
    return render(request,"app/ims.html",{"head":head})
def testing(request):
    head=models.Header.objects.all()
    return render(request,"app/testing.html",{"head":head})

def managed(request):
    head=models.Header.objects.all()
    return render(request,"app/managed.html",{"head":head})

def enterprise(request):
    head=models.Header.objects.all()
    return render(request,"app/enterprise.html",{"head":head})
def captive(request):
    head=models.Header.objects.all()
    return render(request,"app/captive.html",{"head":head})
def strategic(request):
    head=models.Header.objects.all()
    return render(request,"app/strategic.html",{"head":head})
def outsourced(request):
    head=models.Header.objects.all()
    return render(request,"app/outsourced.html",{"head":head})
def system(request):
    head=models.Header.objects.all()
    return render(request,"app/system.html",{"head":head})
def enterprise_solution(request):
    head=models.Header.objects.all()
    return render(request,"app/enterprise_solution.html",{"head":head})
def big_data(request):
    head=models.Header.objects.all()
    return render(request,"app/big_data.html",{"head":head})
def data_science(request):
    head=models.Header.objects.all()
    return render(request,"app/data_science.html",{"head":head})
def social(request):
    head=models.Header.objects.all()
    return render(request,"app/social.html",{"head":head})

def automations(request):
    head=models.Header.objects.all()
    return render(request,"app/automations.html",{"head":head})
def cloud(request):
    head=models.Header.objects.all()
    return render(request,"app/cloud.html",{"head":head})
def mobolity(request):
    head=models.Header.objects.all()
    return render(request,"app/mobility.html",{"head":head})
def robotics(request):
    head=models.Header.objects.all()
    return render(request,"app/robotics.html",{"head":head})
def ibm(request):
    head=models.Header.objects.all()
    return render(request,"app/ibm.html",{"head":head})
def ms_app(request):
    head=models.Header.objects.all()
    return render(request,"app/ms_app.html",{"head":head})
def ms_tech(request):
    head=models.Header.objects.all()
    return render(request,"app/ms_tech.html",{"head":head})
def about(request):
    head=models.Header.objects.all()
    return render(request,"app/about.html",{"head":head})
