from django.http import HttpResponse
from django.shortcuts import render
from .models import Service


def index(request):
    services = Service.objects.all()
    return render(request, 'indexto.html', {'services': services})

