from django.shortcuts import render
from aplicaciones.models import Banco_preguntas
from aplicaciones.models import Curso, Grupos
from aplicaciones.models import Estudiante
# Create your views here.
def inicio(request):
    return render(request, 'Inicio.html')

def crearCurso(request):
    if request.method == "POST":
        newCurso= Curso()
        newCurso.setNombre(request.POST["Curso"])
        newCurso.setDNI(request.POST["idCurso"])
        newCurso.save()
        return render(request, 'CrearCurso.html')
    else:
        return render(request, 'CrearCurso.html')

def verCurso(request):
    return render(request, 'VistaCursos.html')

def crearGrupo(request):
    if request.method == "POST":
        newGrupo= Grupos()
        newGrupo.setNombre(request.POST["Grupo"])
        newGrupo.setDni(request.POST["idGrupo"])
        #Definir curso -> ¿Cómo definir una foreign key?
        newGrupo.save()
        return render(request, 'creargrupo.html')
    else:
        return render(request, 'creargrupo.html')
    

def verGrupo(request):
    return render(request, 'selecciongrupo.html')

def crearBanco(request):
    if request.method == "POST":
        newBanco= Banco_preguntas()
        newBanco.setNombre(request.POST["Banco"])
        newBanco.setDni(request.POST["idBanco"])
        #Definir curso -> ¿Cómo definir una foreign key?
        newBanco.save()
        return render(request, 'crearbanco.html')
    else:
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