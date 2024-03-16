from django.http import HttpResponse


def index(request):
    return HttpResponse("index page")


def login(request):
    return HttpResponse("my login page")