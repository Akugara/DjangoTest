from django.shortcuts import render, redirect
from .models import Estudiante
from .forms import EstudianteRegistrationForm

def estudiante_list(request):
    estudiantes = Estudiante.objects.all()  # Retrieve all estudiantes from the database
    context = {
        'estudiantes': estudiantes
    }
    return render(request, 'estudiantes/estudiantes_list.html', context)

def register_estudiante(request):
    if request.method == 'POST':
        form = EstudianteRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to the estudiantes list page, or wherever is appropriate
            return redirect('estudiantes:estudiante_list')
    else:
        form = EstudianteRegistrationForm()
    return render(request, 'estudiantes/register.html', {'form': form})