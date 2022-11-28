# from django.shortcuts import render
from django.shortcuts import HttpResponse
from .models import user

def accounts_views(request):
    return HttpResponse("this is accounts view page")

