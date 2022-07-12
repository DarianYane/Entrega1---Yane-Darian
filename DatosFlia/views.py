from django.shortcuts import render
#importo las herramientas, models y forms que necesito
from django.http import HttpResponse
from DatosFlia.models import Familiar, Electrodomestico, Vehiculo
from DatosFlia.forms import formFamiliar, formElectrodomestico, formVehiculo, BusquedaFamiliar


# Estas son mis vistas
# Hago las views para listar


def listar_familiar(request):
    context = {
        "familiares": Familiar.objects.all(),
    }
    return render(request,"DatosFlia/familiares.html",context)

def listar_electrodomestico(request):
    contextE = {
        "electrodomesticos": Electrodomestico.objects.all(),
    }
    return render(request,"DatosFlia/electrodomesticos.html",contextE)

def listar_vehiculo(request):
    contextV = {
        "vehiculos": Vehiculo.objects.all(),
    }
    return render(request,"DatosFlia/vehiculos.html",contextV)


# Hago las views para registrar instancias
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


def reg_electrodomestico(request):
    if request.method == "POST":
        miFormulario = formElectrodomestico(request.POST) #Aquí me llaega toda la información del POST
        print(miFormulario)
        if miFormulario.is_valid: # Si pasó la validación de datos de Django
            informacion = miFormulario.cleaned_data # Le doy formato a la informacion
            # Preparo la nueva instancia que será guardada
            nuevoelectrodomestico = Electrodomestico(tipoE=informacion['tipoE'], marcaE=informacion['marcaE'], modeloE=informacion['modeloE'], precio=informacion['precio'], fecha_produccionE=informacion['fecha_produccionE'])
            # Guardo la nueva instancia
            nuevoelectrodomestico.save()
                    
            return render(request,"DatosFlia/regElectrodomestico.html")
        
    else:
        miFormulario=formElectrodomestico() # Form vacio para construir el html        
    
    return render(request,"DatosFlia/regElectrodomestico.html", {"miFormulario":miFormulario})


def reg_vehiculo(request):
    if request.method == "POST":
        miFormulario = formVehiculo(request.POST) #Aquí me llaega toda la información del POST
        print(miFormulario)
        if miFormulario.is_valid: # Si pasó la validación de datos de Django
            informacion = miFormulario.cleaned_data # Le doy formato a la informacion
            # Preparo la nueva instancia que será guardada
            nuevovehiculo = Vehiculo(tipoV=informacion['tipoV'], marcaV=informacion['marcaV'], modeloV=informacion['modeloV'], ruedas=informacion['ruedas'], fecha_produccionV=informacion['fecha_produccionV'])
            # Guardo la nueva instancia
            nuevovehiculo.save()
                    
            return render(request,"DatosFlia/regVehiculo.html")
        
    else:
        miFormulario=formVehiculo() # Form vacio para construir el html        
    
    return render(request,"DatosFlia/regVehiculo.html", {"miFormulario":miFormulario})




# Hago la view de búsqueda

def formulario_busqueda(request):
    formulario_busqueda = BusquedaFamiliar()

    if request.GET:
        queryset = request.GET["nombre"]  
        # Filtro los familiares de la base que tengan el nombre igual al criterio pedido. Y que me traiga todos los de ese tipo
        familiares = Familiar.objects.filter(nombre=queryset).all()

        # Devuelvo lo que encontró
        return render(request, "DatosFlia/busqueda_familiar.html", {"familiares": familiares})

    return render(request, "DatosFlia/busqueda_familiar.html", {"formulario_busqueda": formulario_busqueda})
    

