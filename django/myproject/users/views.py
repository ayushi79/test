from django.shortcuts import render,redirect

# Create your views here.

from django.http import HttpResponse
from .forms import Login,Contact,Signup
from .models import AddUser
from django.core.mail import send_mail
from django.conf import settings
from random import randint

# Create your views here.
def index(request):
    return render(request,"users/index.html")
    #return HttpResponse('Hello World')
def home(request):
    return HttpResponse("<h1 style='color:red'>This is home page</h1>")
def login(request):
    if request.session.get('email'):
        return HttpResponse("Already logged in <a href='/user/logout/'>LOGOUT</a>")  
    form = Login()
    return render(request,"users/login.html",{'f':form})
def afterlogin(request):
    form = Login(request.POST)
    #return HttpResponse(form)
    if form.is_valid():
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']
        try:
            u =AddUser.objects.get(email=email)
        except Exception as e:
            error = 'No Such User.... Signup to login'
            f = Login()
            return render(request,"users/login.html",{'f':f,'error':error})
        else:
            if password == u.password:
                request.session['email'] = email
                pic = u.pic
                
                name = u.username
                email = u.email
                return render(request,"users/afterlogin.html",{'name':name,'email':email,'pic':pic})
                #return HttpResponse('The email is{} password is {} <a href="/user/logout/">Logout</a>'.format(email,password))
            else:
                error = 'Invalid Password'
                form = Login()
                return render(request,'users/login.html',{'f':form,'error':error})

def signup(request):
    form = Signup()
    return render(request,"users/signup.html",{'f':form})
def aftersignup(request):
    form = Signup(request.POST,request.FILES)
    if request.method=="POST":
        if form.is_valid():
            data={
                'username' : form.cleaned_data['username'],
                'email' : form.cleaned_data['email'],
                'password' : form.cleaned_data['password'],
                'pic' : form.cleaned_data['pic']
            }
            #return f'{data}'
            try:
                u = AddUser.objects.get(email=data['email'])
                #return f'{u}'
            except Exception as e:
                newuser = AddUser.objects.create(**data)
                newuser.save()
                f = Login()
                return render(request,'users/login.html',{'f':f})
            else:
                error = 'User already exist'
                f = Signup()
                return render(request,'users/signup.html',{'f':f,'error':error})    
        else:
            error = 'Invalid Form'
            f = Signup()
            return render(request,"users/signup.html",{'error':error,'f':f})

    else:
        error='Invalid method'
        f = Signup()
        return render(request,"users/signup.html",{'error':error,'f':f})
def contact(request):
    form = Contact()
    return render(request,"users/contact.html",{'f':form})
def forgot(request):
    
    from_email = "arpitamishra8102@gmail.com"
    to_email = "nehasaxena683@gmail.com"
    subject = "Mail from django application"
    otp = str(randint(0000,9999))
    message = "Your otp is this " + otp
    send_mail(subject,message,from_email,[to_email,],auth_password=settings.EMAIL_HOST_PASSWORD)
    return HttpResponse("SUCCESS")
def logout(request):
    del request.session['email']
    return redirect('/user/login/')