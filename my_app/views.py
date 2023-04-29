from django.http import HttpResponse 
from django.shortcuts import render
from my_app.models import Person
import datetime

# Create your views here.

def hi_world(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)

def hello_world(request):
    my_data = {
        "name": "Dipankar",
        "tech_stack": "Python",
        "role": "Software developer"
    }
    return render(request, "hello_world.html", context= my_data)

def person_info(request, person_id):
    print('person_id in view ...', person_id)
    person_object = Person.objects.get(id=person_id)
    my_data = {
        "name": person_object.fname + " " + person_object.lname,
        "email": person_object.email,
        "gender": person_object.gender
    }
    return render(request, "person_info.html", context= my_data)

def person_search(request, person_name):
    print('person_id in view ...', person_name)
    try:
        person_object = Person.objects.filter(fname= person_name).first()
    except Person.DoesNotExist:
        # handle the case where no matching objects are found
        person_object = None
    my_data = {
        "name": person_object.fname + " " + person_object.lname,
        "email": person_object.email,
        "gender": person_object.gender
    }
    return render(request, "person_search.html", context= my_data)