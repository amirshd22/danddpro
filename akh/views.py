from django.shortcuts import render, get_object_or_404
from .models import AKHBAR
# Create your views here.
def akhbar(request):
    game = AKHBAR.objects
    return render(request, 'akhbar.html', {'akhbar': game})

def show(request, akhbar_id):
   deli =  get_object_or_404(AKHBAR, pk=akhbar_id)
   return render(request, "dtails.html", {'dtails': deli})