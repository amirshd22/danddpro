from django.shortcuts import render

# Create your views here.

def kharid(request):
    return render(request, 'htcss/kharid.html')