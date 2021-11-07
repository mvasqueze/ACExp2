from django.shortcuts import redirect, render
from aplicaciones.models import Incorrecta, Plantilla, Correcta
from aplicaciones.models import Banco_preguntas
from aplicaciones.models import Curso, Grupos
from aplicaciones.models import Estudiante

# Create your views here.
def inicio(request):
    return render(request, 'Inicio.html')

def crearCurso(request):
    if request.method == "POST":
        newCurso= Curso()
        newCurso.setNombre(request.POST['Curso'])
        newCurso.setDNI(request.POST['idCurso'])
        
        newCurso.save()
        if request.POST.get("CrearU"):
            return redirect('/cursos/')
        return redirect('/crearCurso/')
    else:
        return render(request, 'CrearCurso.html')

def verCurso(request):
<<<<<<< HEAD
    curso_lista=Curso.objects.all()

    return render(request, 'VistaCursos.html', {'curso_lista':curso_lista})
=======
    lista_cursos=Curso.objects.all()
    return render(request, 'VistaCursos.html', {'lista_cursos': lista_cursos })
>>>>>>> 179566d14e645ae001642c67a39989225900bc5b

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

def verBanco(request, dni):
    return render(request, 'seleccionbanco.html')

def crearPlantilla(request):
    if request.method == "POST":
        #banco= Banco_preguntas.objects.get(id=request.POST.get("dni"))
        newPlant= Plantilla()
        #newPlant.id_banco=banco.dni
        newPlant.setdni(request.POST['id_plant'])
        newPlant.setenunciado(request.POST['enunciado'])
        newPlant.save()
        #return redirect('/crearPlantilla/')
        return redirect('/erroneas/')
    else:
        #return render(request, 'crearPlantilla.html')
        return render(request, 'crearPlantilla.html')

def setIncorrectas(request):
    if request.method=="POST":
        #plant=Plantilla.onjects.get(id=request.POST.get("dni"))
        newInc1=Incorrecta()
        #newInc1.id_pregunta=plant.dni
        newInc1.setrespuesta_incorrecta(request.POST['opc1'])
        
        newInc2=Incorrecta()
        #newInc2.id_pregunta=plant.dni
        newInc2.setrespuesta_incorrecta(request.POST['opc2'])
        
        newInc3=Incorrecta()
        #newInc3.id_pregunta=plant.dni
        newInc3.setrespuesta_incorrecta(request.POST['opc3'])
        newInc4=Incorrecta()
        #newInc4.id_pregunta=plant.dni
        newInc4.setrespuesta_incorrecta(request.POST['opc4'])
        newInc5=Incorrecta()
        #newInc5.id_pregunta=plant.dni
        newInc5.setrespuesta_incorrecta(request.POST['opc5'])
        newInc6=Incorrecta()
        #newInc6.id_pregunta=plant.dni
        newInc6.setrespuesta_incorrecta(request.POST['opc6'])
        newInc7=Incorrecta()
        #newInc7.id_pregunta=plant.dni
        newInc7.setrespuesta_incorrecta(request.POST['opc7'])
        newInc1.save()
        newInc2.save()
        newInc3.save()
        newInc4.save()
        newInc5.save()
        newInc6.save()
        newInc7.save()

        return redirect('/variacion/') 
    else:
       return render(request, 'setIncorrectas.html') 

def setVariacion(request):
    if request.method=="POST":
        correcta= Correcta()
        #Falta la ForeignKey
        correcta.setenunciado(request.POST['enunciado'])
        correcta.setrespuesta(request.POST['respuesta'])
        correcta.save()
        if request.POST.get("crearV"):
            return redirect('/variacion/')
        return redirect('/plantillas/')
    else:
        return render(request, 'setVariacion.html')


def verPlantilla(request):
    return render(request, 'plantillas.html')

def estudiantes(request):
    estudiante_lista=Estudiante.objects.all()
    return render(request, 'estudiantes.html', {'estudiante_lista': estudiante_lista })

def crearExamen(request):
    return render(request, 'crearExamenes.html')