from django.shortcuts import render
from aplicaciones.models import Curso
from aplicaciones.models import Estudiante
# Create your views here.
def inicio(request):
    return render(request, 'Inicio.html')

def crearCurso(request):
    if request.method == "POST":
        newCurso= Curso()
        newCurso.nombre=request.POST("Curso")
        #newCurso.setNombre(request.POST["Curso"])
        newCurso.dni=request.POST("idCurso")
        #newCurso.setDNI(request.POST["idCurso"])
        #Definir profe -> ¿Cómo definir una foreign key?
        newCurso.save()
        return render(request, 'CrearCurso.html')
    else:
        return render(request, 'CrearCurso.html')

def verCurso(request):
    return render(request, 'VistaCursos.html')

def crearGrupo(request):
    return render(request, 'creargrupo.html')

def verGrupo(request):
    return render(request, 'selecciongrupo.html')

def crearBanco(request):
    return render(request, 'crearbanco.html')

def verBanco(request):
    return render(request, 'seleccionbanco.html')

def crearPlantilla(request):
    return render(request, 'crearPlantilla.html')

def verPlantilla(request):
    return render(request, 'plantillas.html')

def estudiantes(request):
    estudiante_lista=Estudiante.objects.all()
    return render(request, 'estudiantes.html', {'estudiante_lista': estudiante_lista })

def crearExamen(request):
    return render(request, 'crearExamenes.html')