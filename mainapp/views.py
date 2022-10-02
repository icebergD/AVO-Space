from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, "index.html")

def tutorials(request):
    return HttpResponse("tutorials")

def donate(request):
    return HttpResponse("donate")

def merch(request):
    return render(request, "merch.html")

def login(request):
    return HttpResponse("login")

def signup(request):
    return HttpResponse("signup")



