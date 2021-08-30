from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def projects(request):
    return HttpResponse('Here are our products')

def product(request, pk):
    return HttpResponse('single product'+' '+str(pk))
