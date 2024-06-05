from django.shortcuts import render
from .models import Contact

def home(request):
    contacts = Contact.objects.all()
    return render(request,'poll/home.html', {'contacts': contacts})