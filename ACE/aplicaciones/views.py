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
        curso=Curso.objects.get(dni=request.POST["cursoid"])
        idcurso=request.POST["cursoid"]
        newGrupo= Grupos()
        newGrupo.curso=curso
        newGrupo.setNombre(request.POST["grupo"])
        newGrupo.save()
        return redirect('/grupos/'+idcurso)
    else:
        return render(request,'selecciongrupo.html')
    

def verGrupo(request, dni):
    grupo_lista=Grupos.objects.filter(curso=dni)
    data={}
    data["grupo_lista"]=grupo_lista
    data["curso"]=dni
    return render(request, 'selecciongrupo.html',{"data":data})

def crearBanco(request):
    if request.method == "POST":
        curso=Curso.objects.get(dni=request.POST["cursoid"])
        newBanco= Banco_preguntas()
        newBanco.curso=curso
        newBanco.setnombre(request.POST["Banco"])
        newBanco.setdni(request.POST["idBanco"])
        newBanco.save()
        if request.POST.get("CrearU"):
            return redirect('/crearBanco/')
        elif request.POST.get("CrearV"):
            return redirect('/plantillas/')
        return render(request, 'crearbanco.html',)
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

def estudiantes(request,Grupoid):
    data={}
    data["Grupoid"]=Grupoid
    estudiante_lista=Grupo_estudiantes.objects.filter(id_grupo=Grupoid)
    data["estudiante_lista"]=estudiante_lista
    return render(request, 'estudiantes.html', {'data': data })

def crearEstudiante(request):
    if request.method == "POST":
        grupo=Grupos.objects.get(dni=request.POST["Grupoid"])
        idgrupo=request.POST["Grupoid"]
        newestudiante= Grupo_estudiantes()
        newestudiante.id_grupo=grupo
        newestudiante.setestudiante(request.POST["Estudiante"])
        newestudiante.setId_Estudiante(request.POST["Estudiante_ID"])
        newestudiante.save()
        return redirect('/estudiantes   /'+idgrupo)
    else:
        return render(request, 'estudiantes.html')

def crearExamen(request):
    return render(request, 'crearExamenes.html')