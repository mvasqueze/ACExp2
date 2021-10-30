
from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields.related import ForeignKey
# Create your models here.
class Profe (models.Model):
    dni=models.CharField(max_length=10,primary_key=True)
    nombre = models.CharField(max_length=50)
    def __str__(self):
        texto = "Profe: {0}"
        return texto.format(self.nombre)


class Curso(models.Model):
    dni=models.CharField(max_length=10,primary_key=True)
    nombre = models.CharField(max_length=50)
    profe= models.ForeignKey(Profe,null=False,on_delete=models.CASCADE)
    def __str__(self):
        texto = "Curso: {0}"
        return texto.format(self.nombre)



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
    dni=models.CharField(max_length=10,primary_key=True)
    id_estudiante=models.ForeignKey(Estudiante, null=False, on_delete=CASCADE)
    id_curso=models.ForeignKey(Grupos, null=False, on_delete=CASCADE)


class Banco_preguntas(models.Model):
    dni=models.CharField(max_length=10,primary_key=True)
    nombre = models.CharField(max_length=50)
    curso= models.ForeignKey(Curso,null=False, on_delete=models.CASCADE)
    def __str__(self):
        texto = "Banco de preguntas: {0}"
        return texto.format(self.nombre)


class Plantilla(models.Model):
    dni=models.CharField(max_length=10,primary_key=True)
    nombre = models.CharField(max_length=50)
    id_banco=models.ForeignKey(Banco_preguntas,null=False, on_delete=models.CASCADE)
    enunciado=models.CharField(max_length=500)
    def __str__(self):
        texto = "Pregunta: {0}"
        return texto.format(self.nombre)


class Correcta (models.Model):
    id_pregunta=models.ForeignKey(Plantilla,null=False, on_delete=models.CASCADE)
    enunciado=models.CharField(max_length=50)
    respuesta=models.CharField(max_length=50)

    
class Incorrecta (models.Model):
    id_pregunta=models.ForeignKey(Plantilla,null=False, on_delete=models.CASCADE)
    respuesta_equivocada=models.CharField(max_length=50)

