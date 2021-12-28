from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from calendar import*
# Create your views here.
def  wishes (request):
    return HttpResponse("hello good morning")
def dateandtime(request):
    now=datetime.now()
    return HttpResponse(now)
def monthofcal(request):
    c=HTMLcalandar()
    res=c.formatmonth(2021,8)
    return HttpResponse(res)
