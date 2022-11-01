from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from urllib import request
from django.shortcuts import render, HttpResponse
from home.models import contact
from home.models import blogs
from datetime import datetime
from django.contrib import messages



# Create your views here.
def index(request):
    
    if request.user.is_anonymous:
        return redirect('/login')
    
    return render(request,"index.html")

def loginuser(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('/')
            
        else:
            return render(request,"login.html")
    return render(request,"login.html")

def logoutuser(request):
    logout(request)
    return redirect('/login')

def about(request):
    return render(request,'about.html')
#Services
def services(request):
    return render(request,'colleges.html')
#Contact us
def contacts(request):
    if request.method == "POST":
        name= request.POST.get("name")
        email= request.POST.get("email")
        phone = request.POST.get("phone")
        desc = request.POST.get("desc")
        contacts = contact(name=name,email=email,phone=phone,desc=desc,date=datetime.today())
        contacts.save()
        messages.success(request, 'Your Query has been sent!')
    return render(request,'contact.html')
    
def blog(request):
    if request.method == "POST":
        Authorname= request.POST.get("Authorname")
        title= request.POST.get("title")
        desc = request.POST.get("desc")
        info_blog = blogs(Authorname=Authorname,title=title,desc=desc,date=datetime.today())
        info_blog.save()
        messages.success(request, 'Your Query has been sent!')
   
    return render(request,'blogs.html')

