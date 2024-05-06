from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.

def index(request):
    titulo = 'Titulo de prueba'
    return render(request, 'index.html', {
        'titulo' : titulo
    })