from django.shortcuts import render
from aplicaciones.models import Estudiante
# Create your views here.
def estudiantes(request):
    estudiante_lista=Estudiante.objects.all()
    return render(request, 'estudiantes.html', {'estudiante_lista': estudiante_lista })