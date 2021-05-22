from django.shortcuts import render, HttpResponse
from datetime import datetime
from .models import Contact
from django.contrib import messages
# Create your views here.
def index(request):
    context = {
        'nbar' : "home",
    }
    return render(request, 'index.html', context)
    #return HttpResponse("This is Home Page")
    

def about(request):
    context = {
        'nbar' : "about"
    }
    return render(request, 'about.html', context)
    #return HttpResponse("This is About Page")

def services(request):
    context = {
        'nbar' : "services"
    }
    return render(request, 'services.html', context)
    #return HttpResponse("This is Services Page")

def contact(request):
    context = {
        'nbar' : "contact"
    }
    if request.method == "POST":
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        desc = request.POST.get('desc')
        createdDate = datetime.now()
        contact = Contact(name=name, email=email, phone=phone, desc=desc, createdDate=createdDate)
        contact.save()
        messages.success(request, 'Your message has been sent!') # ignored
    return render(request, 'contact.html', context)
    #return HttpResponse("This is contact Page")
