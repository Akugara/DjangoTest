from django import forms
from .models import Estudiante

class EstudianteRegistrationForm(forms.ModelForm):
    class Meta:
        model = Estudiante
        fields = ['name','surname', 'age', 'gender']