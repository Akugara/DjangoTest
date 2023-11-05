from django.urls import path
from .views import curso_list

app_name = 'cursos'

urlpatterns = [
    path('', curso_list, name='curso_list'),
]
