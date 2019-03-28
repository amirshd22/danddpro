from django.shortcuts import render
from .models import AKHBAR
# Create your views here.
def akhbar(request):
    game = AKHBAR.objects
    return render(request, 'akhbar.html', {'akhbar': game})