from django.shortcuts import render



def home(request):
    return render(request, 'htcss/home.html')


def kharid(request):
    return render(request, 'htcss/kharid.html')

def dar(request):
    return render(request, 'htcss/darbare.html')


def akhbar(request):
    return render(request, 'htcss/akhbar.html')