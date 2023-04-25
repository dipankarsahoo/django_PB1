from django.http import HttpResponse 
from django.shortcuts import render
import datetime

# Create your views here.

def hi_world(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)

def hello_world(request):
    return render(request, "hello_world.html")