from django.shortcuts import render
from .models import AKhbar
# Create your views here.


def akhbar(request):
    akhbar = AKhbar.objects
    return render(request, "akhbar.html", {'job': akhbar})