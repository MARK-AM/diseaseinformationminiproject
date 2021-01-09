from django.shortcuts import render,HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages
from home.models import Info

# Create your views here.
def index(request):
    return render(request,'home.html')
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