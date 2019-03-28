from django.shortcuts import render
from .models import Kharid
# Create your views here.

def kharid(request):
    deli = Kharid.objects
    return render(request, 'kharid.html', {'game': deli })