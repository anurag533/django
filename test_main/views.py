from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(response):
	return HttpResponse("<h1>anurag sharma says hey!</h1>")