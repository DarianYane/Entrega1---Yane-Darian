from django.shortcuts import render
#importo las vistas que necesito
from django.http import HttpResponse
from DatosFlia.models import Familiar


# Estas son mis vistas
# Hago la funcion para listar a los familiares
def listar_familiar(request):
    context = {
        "familiares": Familiar.objects.all(),
    }
    return render(request,"DatosFlia/familiares.html",context)

def reg_familiar(request):
    context = {
        "familiares": Familiar.objects.all(),
    }
    return render(request,"DatosFlia/regFamiliar.html",context)
    
    