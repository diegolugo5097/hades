from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
from core.erp.models import Category, Product


def my_first_view(request):
    data = {
        'name': 'Diego Lugo',
        'categories': Category.objects.all()
    }
    return render(request, 'index.html', data)


def my_second_view(request):
    data = {
        'name': 'Diego Lugo',
        'products': Product.objects.all()
    }
    return render(request, 'second.html', data)
