from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields.related import ForeignKey
import json
# Create your models here.
class Profe (models.Model):
    id=models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
class Curso(models.Model):
    id=id = models.AutoField(primary_key=True) 
    nombre = models.CharField(max_length=50)
    profe= models.ForeignKey(Profe,null=False, blank=False,on_delete=models.CASCADE)

class Grupos(models.Model):
    id=models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    curso= models.ForeignKey(Curso,null=False, blank=False,on_delete=models.CASCADE)
class Estudiante(models.Model):
    id=models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
class Grupo_estudiantes(models.Model):
    id=models.AutoField(primary_key=True)
    id_estudiante=models.ForeignKey(Estudiante, null=False, on_delete=CASCADE)
    id_curso=models.ForeignKey(Grupos, null=False, on_delete=CASCADE)
class Banco_preguntas(models.Model):
    id=models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    curso= models.ForeignKey(Curso,null=False, blank=False,on_delete=models.CASCADE)
class Pregunta(models.Model):
    id=models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    id_banco=models.ForeignKey(Banco_preguntas,null=False, blank=False,on_delete=models.CASCADE)
    json_correctas={}
    correctas=json.dumps(json_correctas,indent=json_correctas.length)
    json_incorrectas={}
    incorrectas=json.dumps(json_incorrectas,indent=json_incorrectas.length)

    