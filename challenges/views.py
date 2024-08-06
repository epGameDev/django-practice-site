from django.shortcuts import render;
from django.http import HttpResponse, HttpResponseNotFound;

# Create your views here.
def index(request):
  return HttpResponse("Hello World!");

def monthly_challenge(request, month):
  return HttpResponse();