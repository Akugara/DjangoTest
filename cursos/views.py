from django.shortcuts import render
from .models import Curso

def curso_list(request):
    cursos = Curso.objects.all()  # Retrieve all cursos from the database
    context = {
        'cursos': cursos
    }
    return render(request, 'cursos/cursos_list.html', context)
