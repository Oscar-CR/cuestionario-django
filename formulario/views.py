from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from .forms import FormularioForm  # Importa el formulario

# Create your views here.

def index(request):
    titulo = 'Titulo de prueba'
    
    form = FormularioForm() 


    return render(request, 'index.html', {
        'titulo' : titulo,
        'form': form,
    })