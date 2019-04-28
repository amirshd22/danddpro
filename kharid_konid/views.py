from django.shortcuts import render,get_object_or_404

from .models import Kharid
# Create your views here.

def kharid(request):
    deli = Kharid.objects
    return render(request, 'kharid.html', {'game': deli })



def show(request, kharid_id):
   deli =  get_object_or_404(Kharid, pk=kharid_id)
   return render(request, "kharids.html", {'kharids': deli})