from django.shortcuts import render
from django.http import HttpResponse
from .forms import Review,Signup,Login
from .models import AddUser
#from django.contrib.auth.models import Team
# Create your views here.

def index(request):
    #return HttpResponse('This is user app')
    return render(request,"users/one.html")
def review(request):
    return render(request,"users/allreview.html")
def signup(request):
    form=Signup()
    return render(request,'users/signup.html',{'f':form})
def aftersignup(request):
    form = Signup(request.POST,request.FILES)
    if request.method=='POST':
        if form.is_valid():
            data = {
                'username':form.cleaned_data['name'],
                'email':form.cleaned_data['email'],
                'password':form.cleaned_data['password'],
                'pic':form.cleaned_data['pic']
            }
            try:
                u = AddUser.objects.get(email=data['email'])
            except Exception as e:
                newuser = AddUser.objects.create(**data)
                newuser.save()
                f = Login()
                return render(request,'users/login.html',{'f':f})
            else:
                error = 'User already exsist'
                f = Signup()
                return render(request,'users/signup.html',{'f':f,'error':error})
        else:
            error = 'Invalid Form'
            f = Signup()
            return render(request,'users/signup.html',{'f':f,'error':error})
    else:
        error = 'Invalid Method'
        f = Signup()
        return render(request,'users/signup.html',{'f':f,'error':error})

def login(request):
    form = Login()
    return render(request,'users/login.html',{'f':form})

def afterlogin(request):
    form = Login(request.POST)
    if form.is_valid():
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']
        try:
            u = AddUser.objects.get(email=email)
        except Exception as e:
            error = 'No such user'
            f = Login()
            return render(request,'users/login.html',{'f':f,'error':error})
        else:
            if password == u.password:
                request.session['email'] = email
                pic = u.pic
                name = u.username
                email = u.email
                return render(request,'users/afterlogin.html',{'name':name,'email':email,'pic':pic})
            else:
                error = 'Invalid Password'
                f = Login()
                return render(request,'users/login.html',{'f':f,'error':error})


def team(request):
    email = AddUser.objects.get(email=request.session.get('email'))
    form = Addteam()
    name = email.username
    return render(request,'users/team.html',{'f':form,'name':name})

def afterteam(request):
    email = AddUser.objects.get(email=request.session.get('email'))
    name = email.username
    form = Addteam(request.POST)
    if request.method=='POST':
        if form.is_valid():
            data = {
                'name' : form.cleaned_data['team'],
                'reason' : form.cleaned_data['reason'],
                'rating' : form.cleaned_data['rating']
            }
            
        
            newuser = Team.objects.create(**data)
            newuser.save()
            f = Addteam()
            return render(request,'users/teams.html',{'name':name,'data':data})
            
        else:
            error = 'Invalid Form'
            f = Addteam()
            return render(request,'users/team.html',{'f':f,'error':error})
    else:
        error = 'Invalid Method'
        f = Addteam()
        return render(request,'users/team.html',{'f':f,'error':error})

    
    


