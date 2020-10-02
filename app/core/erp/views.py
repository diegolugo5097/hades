from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def my_first_view(request):
    return HttpResponse('Hola es mi primera url')


def my_second_view(request):
    return HttpResponse('Hola es mi segunda url')