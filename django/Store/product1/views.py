from django.shortcuts import render
from django.http import HttpResponse

def product_list(request):
    return render(request, 'product1/productPage.html')
