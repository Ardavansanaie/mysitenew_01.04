from django.shortcuts import render
from django.http import HttpResponse



def index_view(request):
    return HttpResponse("hello")


def contact_view(request):
    return HttpResponse("contact")


def about_view(request):
    return HttpResponse("about")
