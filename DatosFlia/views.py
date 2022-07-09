from django.shortcuts import render
#importo las herramientas, models y forms que necesito
from django.http import HttpResponse
from DatosFlia.models import Familiar
from DatosFlia.forms import formFamiliar


# Estas son mis vistas
# Hago la funcion para listar a los familiares
def listar_familiar(request):
    context = {
        "familiares": Familiar.objects.all(),
    }
    return render(request,"DatosFlia/familiares.html",context)

def reg_familiar(request):
    if request.method == "POST":
        miFormulario = formFamiliar(request.POST) #Aquí me llaega toda la información del POST
        print(miFormulario)
        if miFormulario.is_valid: # Si pasó la validación de datos de Django
            informacion = miFormulario.cleaned_data # Le doy formato a la informacion
            # Preparo la nueva instancia que será guardada
            nuevofamiliar = Familiar(nombre=informacion['nombre'], apellido=informacion['apellido'], dni=informacion['dni'], email=informacion['email'], fecha_nacimiento=informacion['fecha_nacimiento'])
            # Guardo la nueva instancia
            nuevofamiliar.save()
                    
            return render(request,"DatosFlia/regFamiliar.html")
        

    else:
        miFormulario=formFamiliar() # Form vacio para construir el html        
    
    return render(request,"DatosFlia/regFamiliar.html", {"miFormulario":miFormulario})

