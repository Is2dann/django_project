from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def portfolio(request):
    return HttpResponse("This page will be a nice gallery of my work, soon.")