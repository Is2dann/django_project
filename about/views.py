from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def about(request):
    return HttpResponse("Hey, I'm Daniel. This page will be all about me soon.")
