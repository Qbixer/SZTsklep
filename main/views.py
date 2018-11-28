from django.shortcuts import render
from django.http import HttpResponse

from .models import Price
# Create your views here.
def contact(request):
  return render(request, 'main/contact.html')

def index(request):
    return render(request, 'main/index.html')

def prices(request):
    prices = Price.objects.order_by('id')
    context = {
        'prices': prices
    }
    return render(request,'main/prices.html',context)
