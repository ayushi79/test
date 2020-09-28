from django.shortcuts import render
from .forms import Blogform
from django.views import View
from .models import Addblog
from django.http import HttpResponse
from users.models import AddUser
from rest_framework.views import APIView
from .serializers import Addblogserializer
from rest_framework.response import Response

# Create your views here.

def addblog(request):
    f = Blogform()
    email = AddUser.objects.get(email=request.session.get('email'))
    t = email.username
    return render(request,'blog/blogform.html',{'f':f,'email':t})

class Blogs(View):
    def get(self,request):
        error = 'Invalid Method'
        f = Blogform()
        return render(request,'blog/blogform.html',{'f':f,'error':error})
    
    def post(self,request):
        f = Blogform(request.POST)
        if f.is_valid():
            data = {
                'author' : AddUser.objects.get(email=request.session.get('email')),
                'title': f.cleaned_data['title'],
                'blog' : f.cleaned_data['blog']
            }
            newblog = Addblog.objects.create(**data)
            newblog.save()
            email = AddUser.objects.get(email=request.session.get('email'))
            t = email.username
            return render(request,'blog/blogform.html',{'f':f,'email':t})
        else:
            error = 'Invalid Form'
            f = Blogform()
            return render(request,'blog/blogform.html',{'f':f,'error':error})

def myblogs(request):
    data = Addblog.objects.all().filter(author=AddUser.objects.get(email=request.session.get('email')))
    #q = data[0]['date']
    return HttpResponse(data)

class showapi(APIView):
    def get(self,request):
        all = Addblog.objects.all()
        blogs = Addblogserializer(all,many=True)
        return Response(blogs.data)

    def post(self,request):
        pass