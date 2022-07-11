"""MVT URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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

# Importo de mi_app.views las vistas (funciones) que necesito
from DatosFlia.views import listar_familiar, reg_familiar, formulario_busqueda, base

urlpatterns = [
    path('admin/', admin.site.urls),
    #Agrego los path que necesito 
    path('familiares/', listar_familiar),
    path('regFamiliar/', reg_familiar),
    path('buscar/', formulario_busqueda),
    path('base/', base)
]
