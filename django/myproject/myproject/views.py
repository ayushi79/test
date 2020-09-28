from django.http import HttpResponse
def index(request):
    return HttpResponse('Hello World')
def home(request):
    return HttpResponse("<h1 style='color:red'>Welcome</h1>")