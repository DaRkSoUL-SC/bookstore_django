from django.shortcuts import render,redirect
from django.http import HttpResponse
from app2.models import book
from django.contrib.auth.forms import UserCreationForm  
from django.contrib.auth.models import User 
from .forms import booksregistration,contactform
from django.contrib.auth import login, authenticate #add this
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.
def index(request):
    return render(request,'index.html')

def bookform(request):
    return render(request,'addbook.html')

def addbook(request):
    if request.method=="POST":
        w=request.POST['bname']
        x=request.POST['aname']
        y=request.POST['bdesc']
        z=request.POST['bprice']
        c1=book.objects.create(bname=w,aname=x,bdesc=y,bprice=z)
        c1.save()
        return redirect('/dashboard')
    
def getbook(request):
    content={}
    content['data']=book.objects.all()
    return render(request,'dashboard.html',content)

def edit(request,rid):
    if request.method=='POST':
        w=request.POST['bname']   
        x=request.POST['aname']  
        y=request.POST['bdesc']  
        z=request.POST['bprice']  
        c=book.objects.filter(id=rid)
        c.update(bname=w,aname=x,bdesc=y,bprice=z)
        return redirect('/dashboard')
    else:
        content={}
        content['x']=book.objects.get(id=rid)
        return render(request,'editbook.html',content)
    
def delete(reqeust,rid):   
    x=book.objects.get(id=rid)    
    x.delete()
    return redirect('/dashboard')

    
def home(request):
    return render(request,'bookstore.html')

def books(request):
    content={}
    content['data']=book.objects.all()
    return render(request,'books.html',content)

def register(request):
    if request.method=="POST":
        fm=UserCreationForm(request.POST)
        if fm.is_valid():
            fm.save()
            return redirect("/")
    else:
        fm=UserCreationForm()
    return render(request,'register.html',{'form':fm})

def login_user(request):
    if request.method=="POST":
        fm = AuthenticationForm(request, data=request.POST)
        if fm.is_valid():
            username = fm.cleaned_data.get('username')
            password = fm.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("/dashboard")
            else:
                 messages.error(request,"Invalid username or password.")
                 
        else:
            messages.error(request,"Invalid username or password.")
    fm = AuthenticationForm()
    return render(request,'login.html',{'form':fm})

def contact(request):
    context={}
    form =contactform(request.POST)
    if form.is_valid():
        form.save()

    context['form']=form
    return render (request,'contact.html',context)