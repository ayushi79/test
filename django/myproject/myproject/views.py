from django.http import HttpResponse

def index(request):
    return HttpResponse('hello! welcome')
def home(request):
    return HttpResponse('Thanku for visit again')