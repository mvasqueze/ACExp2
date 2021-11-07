from django.shortcuts import redirect, render
from ACE.aplicaciones.models import Grupo_estudiantes
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
        if request.POST.get("CrearU"):
            return redirect('/cursos/')
        return redirect('/crearCurso/')
    else:
        return render(request, 'CrearCurso.html')

def verCurso(request):
    curso_lista=Curso.objects.all()
    return render(request, 'VistaCursos.html', {'curso_lista':curso_lista})

def crearGrupo(request):
    if request.method == "POST":
        newGrupo= Grupos()
        newGrupo.setNombre(request.POST["Grupos"])
        newGrupo.setDni(request.POST["idGrupo"])
        #Definir curso -> ¿Cómo definir una foreign key?
        newGrupo.save()
        return render(request, 'creargrupo.html')
    else:
        return render(request, 'creargrupo.html')
    

def verGrupo(request, dni):
    grupo_lista=Grupos.objects.filter(curso=dni)
    return render(request, 'selecciongrupo.html', {'grupo_lista':grupo_lista})

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

def estudiantes(request,cursoid):
    estudiante_lista=Grupo_estudiantes.objects.filter(id_curso=cursoid)
    return render(request, 'estudiantes.html', {'estudiante_lista': estudiante_lista })

def crearEstudiante(request,cursoid):
    if request.method == "POST":
        curso=Curso.objects.get(dni=cursoid)
        newBanco= Grupo_estudiantes()
        newBanco.setestudiante(request.POST["Nombre"])
        newBanco.setId_Estudiante(request.POST["idEstudiante"])
        newBanco.save()
        return redirect(request, '')
    else:
        return render(request, 'crearEstudiante.html')

def crearExamen(request):
    return render(request, 'crearExamenes.html')