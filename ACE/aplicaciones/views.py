from django.shortcuts import redirect, render
from aplicaciones.models import Grupo_estudiantes
from aplicaciones.models import Banco_preguntas
from aplicaciones.models import Curso, Grupos
from aplicaciones.models import Incorrecta, Plantilla, Correcta

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
    curso_lista=Curso.objects.all()
    return render(request, 'VistaCursos.html', {'curso_lista':curso_lista})


def crearGrupo(request):
    if request.method == "POST":
        newGrupo= Grupos()
        newGrupo.setNombre(request.POST["Grupos"])
        newGrupo.setDni(request.POST["idGrupo"])
        newGrupo.save()
        return render(request, 'creargrupo.html')
    else:
        return render(request, 'creargrupo.html')
    

def verGrupo(request, dni):
    grupo_lista=Grupos.objects.filter(curso=dni)
    data={}
    data["curso"]=dni
    return render(request, 'selecciongrupo.html', {'grupo_lista':grupo_lista},{"data":data})

def crearBanco(request):
    if request.method == "POST":
        curso=Curso.objects.get(dni=request.POST["cursoid"])
        newBanco= Banco_preguntas()
        newBanco.curso=curso
        newBanco.setnombre(request.POST["Banco"])
        newBanco.setdni(request.POST["idBanco"])
        newBanco.save()
        return redirect('/bancos/'+request.POST["cursoid"])
    else:
        return render(request, 'crearbanco.html')

def verBanco(request, dni):
    Banco_lista= Banco_preguntas.objects.filter(curso=dni)
    data={}
    data["Banco_lista"]=Banco_lista
    data["curso"]=dni
    return render(request, 'seleccionbanco.html',{"data":data})

def crearPlantilla(request):
    if request.method == "POST":
        banco= Banco_preguntas.objects.get(dni=request.POST["bancoid"])
        newPlant= Plantilla()
        newPlant.id_banco=banco
        newPlant.setdni(request.POST['id_plant'])
        newPlant.setenunciado(request.POST['enunciado'])
        newPlant.save()
        #return redirect('/crearPlantilla/')
        if request.POST.get("CrearU"):
            return redirect('/variacion/'+request.POST["id_plant"])
        elif request.POST.get("CrearV"):
            return redirect('/plantillas/'+request.POST["bancoid"])
        return render(request, 'plantillas.html',)
    else:
        #return render(request, 'crearPlantilla.html')
        return render(request, 'crearPlantilla.html')

def verPlantilla(request, dni):
    plant_lista= Plantilla.objects.filter(id_banco=dni)
    data={}
    data["plant_lista"]=plant_lista
    data["banco"]=dni
    return render(request, 'plantillas.html',{"data":data})


def verIncorrectas(request, plantillaid):
    data={}
    data["plantillaid"]=plantillaid
    lista_Incorrectas=Incorrecta.objects.filter(id_pregunta=plantillaid)
    data["lista_Incorrectas"]=lista_Incorrectas
    return render(request,'',{"data":data})


def setIncorrectas(request):
    if request.method=="POST":
        plantilla=Plantilla.objects.get(dni=request.POST["plantillaid"])
        newInc1=Incorrecta()
        newInc1.id_pregunta=plantilla
        newInc1.setrespuesta_incorrecta(request.POST['opc1'])
        newInc2=Incorrecta()
        newInc2.id_pregunta=plantilla
        newInc2.setrespuesta_incorrecta(request.POST['opc2'])
        newInc3=Incorrecta()
        newInc3.id_pregunta=plantilla
        newInc3.setrespuesta_incorrecta(request.POST['opc3'])
        newInc4=Incorrecta()
        newInc4.id_pregunta=plantilla
        newInc4.setrespuesta_incorrecta(request.POST['opc4'])
        newInc5=Incorrecta()
        newInc5.id_pregunta=plantilla
        newInc5.setrespuesta_incorrecta(request.POST['opc5'])
        newInc6=Incorrecta()
        newInc6.id_pregunta=plantilla
        newInc6.setrespuesta_incorrecta(request.POST['opc6'])
        newInc7=Incorrecta()
        newInc7.id_pregunta=plantilla
        newInc7.setrespuesta_incorrecta(request.POST['opc7'])
        newInc1.save()
        newInc2.save()
        newInc3.save()
        newInc4.save()
        newInc5.save()
        newInc6.save()
        newInc7.save()

        return redirect('/plantillas/') 
    else:
       return render(request, 'setIncorrectas.html') 

def setVariacion(request):
    if request.method=="POST":
        plant= Plantilla.objects.get(dni=request.POST["preguntaid"])
        correcta= Correcta()
        correcta.id_pregunta=plant
        correcta.setenunciado(request.POST['enunciado'])
        correcta.setrespuesta(request.POST['respuesta'])
        correcta.save()
        if request.POST.get("crear1"):
            return redirect('/erroneas/'+request.POST["preguntaid"])
        return redirect('/variacion/'+request.POST["preguntaid"])
    else:
        return render(request, 'setVariacion.html')

def verVar(request, dni):
    var_lista=Correcta.objects.filter(id_pregunta=dni)
    data={}
    data["lista_correctas"]=var_lista
    data["id_pregunta"]=dni
    return render(request, 'setVariacion.html',{"data":data})

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