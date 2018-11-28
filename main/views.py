from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def contact(request):
  return render(request, 'main/contact.html')

def index(request):
    return render(request, 'main/index.html')

def prices(request):
    return render(request,'main/prices.html')
