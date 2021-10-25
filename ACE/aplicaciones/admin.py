from django.contrib import admin

from aplicaciones.models import Curso, Profe, Grupos, Grupo_estudiantes, Estudiante, Banco_preguntas,Pregunta
# Register your models here.
admin.site.register(Curso)
admin.site.register(Pregunta)
admin.site.register(Profe)
admin.site.register(Grupo_estudiantes)
admin.site.register(Grupos)
admin.site.register(Estudiante)
admin.site.register(Banco_preguntas)
