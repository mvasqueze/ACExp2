from django.contrib import admin
from aplicaciones.models import Curso, Grupos, Grupo_estudiantes, Estudiante, Banco_preguntas,Plantilla,Correcta,Incorrecta
# Register your models here.
admin.site.register(Curso)
admin.site.register(Plantilla)
admin.site.register(Grupo_estudiantes)
admin.site.register(Grupos)
admin.site.register(Estudiante)
admin.site.register(Banco_preguntas)
admin.site.register(Correcta)
admin.site.register(Incorrecta)

