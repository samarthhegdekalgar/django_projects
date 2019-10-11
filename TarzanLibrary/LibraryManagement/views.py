from django.shortcuts import render
from django.http import HttpResponse


def home_page(request):
    return HttpResponse('<h1><center>Welcome to TarzanSkills book collections</center></h1>')
