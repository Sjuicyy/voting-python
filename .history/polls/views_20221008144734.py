from http.client import HTTPResponse
from django.shortcuts import render
from django.urls import 

# Create your views here.

def index(request):
    return HTTPResponse("hello world . You're at the polls index.")

