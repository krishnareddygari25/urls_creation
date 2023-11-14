from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def sharma(request):
    return render(request,'sharma.html')
def  indian(request):
    return HttpResponse('<h1>best bastsman</h1')