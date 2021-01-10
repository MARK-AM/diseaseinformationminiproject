from django.shortcuts import render,redirect
from datetime import datetime
from home.models import *
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from home.forms import CreateUserform
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def index(request):
   return render(request,'home.html')

def welcome(request):
    allnewss = News.objects.all()
    param = {'allnewss': allnewss}
    return render(request, 'welcome.html', param)

def about(request):
    return render(request,'about.html')
def contact(request):
    return render(request,'contact.html')
def submitcontact(request):
    if request.method=='POST':
        gname = request.POST.get('name')
        gemail = request.POST.get('email')
        gmsg = request.POST.get('msg')
        if gname!='' and gemail!='' and gmsg!='':
            contact = Contact(name=gname, email=gemail, msg=gmsg, date=datetime.today())
            contact.save()
            messages.success(request,"Thanks for contacting us...")
            return render(request,'submitcontact.html')
        messages.success(request,"Something went wrong.Check whether you have filled all "
                               "information in the form and try again")
        return render(request,'submitcontact.html')

def disease(request):
    allInfos = Info.objects.all()
    print(allInfos)
    context = {'allInfos': allInfos}
    return render(request,'disease.html',context)

def search(request):
    query=request.GET['query']
    allInfos=Info.objects.filter(name__icontains=query)
    params={'allInfos': allInfos }
    return render(request,'search.html', params)
    #disease_names= ["heart", "disease","cancer","typhoid",]

def home1(request):
    return render(request,"home1.html")

def whatisdisease(request):
    return render(request,"whatisdisease.html")

def registerPage(request):
    if request.user.is_authenticated:
        return redirect('welcome')
    else:
        form=CreateUserform()

        if request.method=='POST':
            form=CreateUserform(request.POST)
            if form.is_valid():
                form.save()
                user=form.cleaned_data.get('username')
                messages.success(request,'Account was created for '+ user)
                return redirect('login')

    context={'form':form}
    return render(request,'register.html',context)

def loginPage(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')

        user=authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect('welcome')
        else:
            messages.info(request,"Username OR Password is incorrect")
    context={}
    return render(request,'login.html',context)

def logoutUser(request):
    logout(request)
    return redirect('login')