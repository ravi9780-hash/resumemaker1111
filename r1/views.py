from django.shortcuts import render
import time
from .forms import imgform

# Create your views here.
def home(request):
    return render(request,'home.html')
def temp(request):
    return render(request,'temp.html')
def withoutimg(request):
    return render(request,'withoutimage.html')
def try1(request):
    if request.method=='POST':
       name=request.POST['name']
       jobt=request.POST['jobtitle']
       profile=request.POST['profile']
       Experience=request.POST['Experience']
       hobbies=request.POST['hobbies']
       position=request.POST['positions']
       lasteducation=request.POST['lasteducation']
       university=request.POST['university']
       skills=request.POST['skills']
       paasout=request.POST['passout']
       mobile=request.POST['mobile']
       email=request.POST['email']
       country=request.POST['country']
       linkedin=request.POST['linkedin']
       newhobbies=hobbies.split(',')
       newposition=position.split(',')
       newskills=skills.split(',')
       print(newskills)
       print(newhobbies)
       print(newposition)
       return render(request,'tr.html',{'name':name,'jobt':jobt,'profile':profile,'Experience':Experience,'hobbies':newhobbies,'position':newposition,'skills':newskills,'passout':paasout,'mobile':mobile,'lasteducation':lasteducation,'email':email,'country':country,'linkedin':linkedin,'university':university})
    return render(request,'fill.html')

def withimage(request):
    if request.method=='POST':
        name=request.POST['name']
        jobt=request.POST['jobtitle']
        profile=request.POST['profile']
        Experience=request.POST['Experience']
        hobbies=request.POST['hobbies']
        position=request.POST['positions']
        lasteducation=request.POST['lasteducation']
        university=request.POST['university']
        skills=request.POST['skills']
        paasout=request.POST['passout']
        mobile=request.POST['mobile']
        email=request.POST['email']
        country=request.POST['country']
        linkedin=request.POST['linkedin']
        newhobbies=hobbies.split(',')
        newposition=position.split(',')
        newskills=skills.split(',')
        print(newskills)
        print(newhobbies)
        print(newposition)
        return render(request,'withimage.html',{'name':name,'jobt':jobt,'profile':profile,'Experience':Experience,'hobbies':newhobbies,'position':newposition,'skills':newskills,'passout':paasout,'mobile':mobile,'lasteducation':lasteducation,'email':email,'country':country,'linkedin':linkedin,'university':university})
    else:
        form=imgform()
    return render(request,'fill1.html',{'form':form})

