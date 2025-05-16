from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.

def people(request):
    return HttpResponse("Welcome To The Page")

def python_first_app(request):
    return HttpResponse("Congratulations..!! You Have Created Your Fist App" )

def patients(response):
    template = loader.get_template('patients.html')
    return HttpResponse(template.render())