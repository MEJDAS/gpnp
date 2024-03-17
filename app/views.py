from django.http import HttpResponse
from django.shortcuts import render
from .models import Member

def index(request):
    return render(request,"pages/index.html")


def login(request):
    return render(request,"pages/login.html")



def teamMenu(request):
    members = Member.objects.all()
    return render(request,"pages/team-menu.html",{'members': members})


def requestMenu(request):
    return render(request,"pages/request-menu.html")


def reportMenu(request):
    return render(request,"pages/report-menu.html")


def departement(request):
    return render(request,"pages/departement.html")

