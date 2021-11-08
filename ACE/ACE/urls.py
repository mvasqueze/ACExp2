"""ACE URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from aplicaciones.views import *
from django.urls.conf import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('inicio/', inicio),
    path('cursos/', verCurso,),
    path('crearCurso/', crearCurso, name="crearCurso"),
    path('bancos/<dni>', verBanco),
    path('crearBanco/', crearBanco, name="crearBanco"),
    path('grupos/<dni>', verGrupo),
    path('crearGrupo/', crearGrupo),
    path('plantillas/<dni>', verPlantilla),
    path('crearPlantilla/', crearPlantilla, name="crearPlantilla"),
    path('estudiantes/', estudiantes),
    path('crearExamen/', crearExamen),
    path('erroneas/', setIncorrectas, name="setIncorrectas"),
    path('variacion/<dni>', verVar, name="verVar"),
    path('setVariacion/', setVariacion, name="setVariacion"),
    path('accounts/',include('django.contrib.auth.urls')),
    path('crearEstudiantes/<idcurso>',crearEstudiante, name="crearEstudiante"),
    path('listaerroneas/<idcurso>',crearEstudiante, name="listaerroneas"),
]