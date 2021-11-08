
from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields.related import ForeignKey
# Create your models here.



class Curso(models.Model):
    dni=models.CharField(max_length=10,primary_key=True)
    nombre = models.CharField(max_length=50)
    def __str__(self):
        texto = "Curso: {0}"
        return texto.format(self.nombre)
    
    def setDNI(self, dni):
        self.dni=dni
    
    def setNombre(self, nombre):
        self.nombre=nombre

    def getDNI(self):
        return self.dni

    def getNombre(self):
        return self.nombre

   

class Grupos(models.Model):
    dni=models.CharField(max_length=10,primary_key=True)
    nombre = models.CharField(max_length=50)
    curso= models.ForeignKey(Curso,null=False, on_delete=models.CASCADE)
    def __str__(self):
        texto = "Grupo: {0}"
        return texto.format(self.nombre)
    
    def getDni(self):
        return self.dni
    
    def getNombre(self):
        return self.nombre
    
    def getCurso(self):
        return self.curso
    
    def setDni(self, dni):
        self.dni = dni
    
    def setNombre(self, nombre):
        self.nombre = nombre
    
    def setCurso(self, curso):
        self.curso = curso


class Estudiante(models.Model):
    dni=models.CharField(max_length=10,primary_key=True)
    nombre = models.CharField(max_length=50)
    
    def __str__(self):
        texto = "Estudiante: {0}"
        return texto.format(self.nombre)
    
    def getDni(self):
        return self.dni
    
    def getNombre(self):
        return self.nombre

    def setDni(self, dni):
        self.dni = dni

    def setNombre(self, nombre):
        self.nombre = nombre


class Grupo_estudiantes(models.Model):
    dni=models.AutoField(max_length=10,primary_key=True)
    id_estudiante=models.CharField(max_length=10)
    nombre_estudiante=models.CharField(max_length=20)
    id_curso=models.ForeignKey(Grupos, null=False, on_delete=CASCADE)
    def __str__(self):
        texto = "Estudainte: {0}, Curso:{1}"
        return texto.format(self.nombre_estudiante,self.id_estudiante)
    def getdni(self):
        return self.dni
    def getid_estudiante(self):
        return self.id_estudiante
    def getid_curso(self):
        return self.id_curso
    def getestudiante(self):
        return self.nombre_estudiante
    def setestudiante(self,estudiante):
        self.nombre_estudiante=estudiante
    def setId_Estudiante(self,id):
        self.id_estudiante=id



class Banco_preguntas(models.Model):
    dni=models.CharField(max_length=10,primary_key=True)
    nombre = models.CharField(max_length=50)
    curso= models.ForeignKey(Curso,null=False, on_delete=models.CASCADE)
    def __str__(self):
        texto = "Banco de preguntas: {0}"
        return texto.format(self.nombre)
    def getdni(self):
        return self.dni
    def getnombre(self):
        return self.nombre
    def getid_curso(self):
        return self.curso
    def setdni(self,dni):
        self.dni=dni
    def setnombre(self,nombre):
        self.nombre=nombre 


class Plantilla(models.Model):
    dni=models.CharField(max_length=10,primary_key=True)
    #id_banco=models.ForeignKey(Banco_preguntas,null=False, on_delete=models.CASCADE)
    enunciado=models.CharField(max_length=500)

    def __str__(self):
        texto = "Pregunta: {0} - Enunciado: {1}"
        return texto.format(self.dni, self.enunciado)

    def getdni(self):
        return self.dni
        

        
    def getid_banco(self):
        return self.id_banco
        
    def getenunciado(self):
        return self.enunciado
        
    def setdni(self, dni):
        self.dni=dni


    def setenunciado(self, enunciado):
        self.enunciado=enunciado

    def setVariaciones(self, variaciones):
        self.variaciones=variaciones

class Correcta (models.Model):
    id_pregunta=models.ForeignKey(Plantilla, blank=True, null=True, on_delete=models.CASCADE)
    enunciado=models.CharField(max_length=50)
    respuesta=models.CharField(max_length=50)

    def getid_pregunta(self):
        return self.id_pregunta

    def getenunciado(self):
        return self.enunciado

    def getrespuesta(self):
        return self.respuesta

    def setenunciado(self, enunciado):
        self.enunciado=enunciado

    def setrespuesta(self, respuesta):
        self.respuesta=respuesta

    
class Incorrecta (models.Model):
    id_pregunta=models.ForeignKey("Plantilla", blank=True, null=True, on_delete=models.CASCADE)
    respuesta_equivocada=models.CharField(max_length=50,  blank=True, default='')
    def getid_pregunta(self):
        return self.id_pregunta

    def getrespuesta_equivocada(self):
        return self.respuesta_equivocada

    def setrespuesta_incorrecta(self, respuesta_incorrecta):
        self.respuesta_equivocada=respuesta_incorrecta
