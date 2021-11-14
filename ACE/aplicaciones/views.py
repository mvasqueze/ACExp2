from django.shortcuts import redirect, render
from aplicaciones.models import Grupo_estudiantes
from aplicaciones.models import Banco_preguntas
from aplicaciones.models import Curso, Grupos
from aplicaciones.models import Incorrecta, Plantilla, Correcta
from reportlab.pdfgen import canvas
from django.http import FileResponse, response
import io
import zipfile
from django.http import HttpResponse
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter
import random

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
        return redirect('/bancos/'+request.POST["cursoid"])
    else:
        return render(request, 'crearbanco.html')

def verBanco(request, dni):
    Banco_lista= Banco_preguntas.objects.filter(curso=dni)
    data={}
    data["Banco_lista"]=Banco_lista
    data["curso"]=dni
    return render(request, 'seleccionbanco.html',{"data":data})

def deletebanco(request):
    banco= Banco_preguntas.objects.get(dni=request.POST["bancoid"])
    banco.delete()
    curso=banco.getid_curso()
    cursoid=curso.getDNI()
    return redirect('/bancos/'+cursoid)

def deletecurso(request):
    curso=Curso.objects.get(dni=request.POST["cursoidborrar"])
    curso.delete()
    return redirect('/cursos/')

def deletegrupo(request):
    grupo=Grupos.objects.get(dni=request.POST["Grupoidborrar"])
    curso=grupo.getCurso()
    cursoid=curso.getDNI()
    grupo.delete()
    return redirect('/grupos/'+cursoid)

def deleteestudiante(request):
    grupo=request.POST["Grupo"]
    dniEstudiante=request.POST["Estudiante_ID_borrar"]
    estudiante=Grupo_estudiantes.objects.get(id_estudiante=dniEstudiante)
    estudiante.delete()
    return redirect('/estudiantes/'+grupo)

def deletevariacion(request):
    grupo=request.POST["Grupo"]
    dniEstudiante=request.POST["Estudiante_ID_borrar"]
    estudiante=Grupo_estudiantes.objects.get(id_estudiante=dniEstudiante)
    estudiante.delete()
    return redirect('/estudiantes/'+grupo)

def deleteplantilla(request):
    preguntaid=request.POST["preguntaid"]
    plantilla=Plantilla.objects.get(dni=preguntaid)
    Banco=plantilla.getid_banco()
    idbanco=Banco.getdni()
    plantilla.delete()
    return redirect('/plantillas/'+idbanco)

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
    return render(request,'setIncorrectas.html',{"data":data})


def setIncorrectas(request):
    if request.method=="POST":
        plantilla=Plantilla.objects.get(dni=request.POST["plantillaid"])
        banco=plantilla.getid_banco()
        bancoid=banco.getdni()
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

        return redirect('/plantillas/'+bancoid) 
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
            return redirect('/listaerroneas/'+request.POST["preguntaid"])
        return redirect('/variacion/'+request.POST["preguntaid"])
    else:
        return render(request, 'setVariacion.html')

def verVar(request, dni):
    var_lista=Correcta.objects.filter(id_pregunta=dni)
    data={}
    data["lista_correctas"]=var_lista
    data["id_pregunta"]=dni
    return render(request, 'setVariacion.html',{"data":data})

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
        return redirect('/estudiantes/'+idgrupo)
    else:
        return render(request, 'estudiantes.html')

def verExamen(request,idgrupo):
    data={}
    data["idgrupo"]=idgrupo
    return render(request, 'crearExamenes.html',{"data":data})

def crearExamen(request):
    #Creacion zip
    responseZ = HttpResponse(content_type='application/zip')
    zf=zipfile.ZipFile(responseZ, 'w')
    #Llamados varios
    grupoid=request.POST["grupoid"]
    estudiante_lista=Grupo_estudiantes.objects.filter(id_grupo=grupoid)
    nombre_banco=request.POST["Banco_examen"]
    banco=Banco_preguntas.objects.get(nombre=nombre_banco)
    idbanco=banco.getdni()
    cantidad=request.POST["cantPreguntas"]
    #pdf solucionario
    responseP= HttpResponse(content_type='application/pdf')
    responseP['Content-Disposition']='attachment; filename=solucionario.pdf'
    solucionario=canvas.Canvas(responseP)
    #pdf lista de estudiantes
    #buf=io.BytesIO()
    responseL= HttpResponse(content_type='application/pdf')
    responseL['Content-Disposition']='attachment; filename=listaEstudiantes.pdf'
    listaE=canvas.Canvas(responseL, pagesize=letter, bottomup=0)
    textobL=listaE.beginText()
    textobL.setTextOrigin(inch, inch)
    textobL.setFont("Times-Roman", 11)
    #Lista auxiliar de la lista de estudiantes
    listaEstudiantes=[]
    for i in range(len(estudiante_lista)):
        nombreEid= "Nombre:" + estudiante_lista[i].nombre_estudiante + "  id:" + estudiante_lista[i].id_estudiante
        listaEstudiantes.append(nombreEid)
    for line in listaEstudiantes:
        textobL.textLine(line)
    listaE.drawText(textobL)
    #loop de la creacion de examanes para cada estudiante
    for i in range(len(estudiante_lista)):
        responseE= HttpResponse(content_type='application/pdf')
        filename=estudiante_lista[i].nombre_estudiante+'.pdf'
        responseE['Content-Disposition']='attachment; filename="{}"'.format(filename)
        examen=canvas.Canvas(responseE)
        solucionario.setFont("Times-Roman", 11)
        examen.setFont("Times-Roman", 11)
        solucionario.drawString(0,2.5*inch , listaEstudiantes[i])
        examen.drawString(0,2.5*inch , listaEstudiantes[i])
        aux=autoExam(idbanco, cantidad)
        examen.drawString(0,2.5*inch , aux.values())
        solucionario.drawString(0,2.5*inch , aux.keys())
        examen.save()
        zf.writestr(examen)
    solucionario.save()
    zf.writestr(solucionario, listaE)
    responseZ['Content-Disposition']=f'attachment; filename="Examenes.zip"'
    #coger cantidad que decidamos de plantillas de manera al azar y guardarlas en una lista o diccionario
    #declarar un string que sea igual a "enunciado" de la plantilla
    #conseguir una opcion de la plantilla de manera al azar (recomendacion pedir todas las relacionadas con la plantilla que se esta trabajando y usar un metodo que coja una al azar)
    #declarar un string que sea igual a "enunciado" de la opcion obtenida
    #declarar un string que sea igual a "respuesta" de la opcion obtenida
    #pedir la cantidad especifica de incorrectas que se van a usar
    #pedir todas las incorrectas relacionadas con esa plantilla 
    #almacenar la cantidad decidida de incorrectas elegidas al azar en una lista o diccionario
    #crear un string que junte los dos enunciados 
    #añadir el string de los dos enunciados +  la respuesta correcta en otro pdf
    #añadir al pdf del examen el enunciado combinado
    #añadir de forma aletoria las incorrectas y las correctas de la pregunta
    #repetir con las demas plantillas
    #repetir con todos los estudiantes del grupo seleccionado
    return(responseZ)
    

def autoExam(banco, cantidad):
    plant_lista= Plantilla.objects.filter(id_banco=banco)
    #lista_Incorrectas=Incorrecta.objects.filter(id_pregunta=plant_lista.dni)
    
    imp={}
    listaSol=[]
    listaPreg=[]
    i=0
    while i< int(cantidad):
        #sol es el string del solucionario
        sol=""
        #numero aleatorio para sacar una plantilla
        n=random.randint(0, len(plant_lista)-1)
        enun=plant_lista[n]
        #lista de variaciones
        list_variacion=Correcta.objects.filter(id_pregunta=plant_lista[n].dni)
        #lista de incorrectas
        listPID=[]
        aux1=Incorrecta.objects.filter(id=plant_lista[n].dni)
        for j in range(len(aux1)):
            aux2=aux1[j].respuesta_equivocada
            listPID.append(aux2)
        ranVar=random.randint(0, len(list_variacion)-1)
        variacion=list_variacion[ranVar]
        sol=enun.enunciado.replace('///', variacion.enunciado)+'\n'+variacion.respuesta
        random.shuffle(listPID)
        listaResp=[variacion.respuesta]
        for resp in listPID:
            listaResp.append(resp)
        aux=0
        while aux>3:
            listaResp.append(listPID[aux])
            aux=aux+1
        pregunta= str(i) + ') ' + enun.enunciado.replace('///', variacion.enunciado) + '\n' + listaResp[0] + '\n' + listaResp[1] + '\n' + listaResp[2] + '\n' + listaResp[3] + '\n'
        listaSol.append(sol)
        listaPreg.append(pregunta)
    imp.update({listaSol:listaPreg})
    return imp