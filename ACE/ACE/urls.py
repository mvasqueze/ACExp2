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
<<<<<<< HEAD
from aplicaciones.views import *
=======
from django.urls.conf import include
from aplicaciones.views import estudiantes
>>>>>>> afafa7c59707d070aebc91022b69b7fea7807c21

urlpatterns = [
    path('admin/', admin.site.urls),
    path('inicio/', admin.site.urls),
    path('cursos/', admin.site.urls),
    path('crearCurso/', admin.site.urls),
    path('bancos/', admin.site.urls),
    path('crearBanco/', admin.site.urls),
    path('grupos/', admin.site.urls),
    path('crearGrupo/', admin.site.urls),
    path('plantillas/', admin.site.urls),
    path('crearPlantilla/', admin.site.urls),
    path('estudiantes/', estudiantes),
<<<<<<< HEAD
]
=======
    path('accounts/',include('django.contrib.auth.urls')),
]
>>>>>>> afafa7c59707d070aebc91022b69b7fea7807c21
