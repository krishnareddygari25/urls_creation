from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def msd(request):
    return render(request,'virat.html')
def  dhoni(request):
    return HttpResponse('<h1>best bastsman</h1')