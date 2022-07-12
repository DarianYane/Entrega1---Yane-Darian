from django import forms

class formFamiliar(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    dni = forms.IntegerField()
    email = forms.EmailField()
    fecha_nacimiento = forms.DateField() #(YYYY-MM-DD)

class formElectrodomestico(forms.Form):
    tipoE = forms.CharField()
    marcaE = forms.CharField()
    modeloE = forms.CharField()
    precio = forms.IntegerField()
    #email = forms.EmailField()
    fecha_produccionE = forms.DateField() #(YYYY-MM-DD)

class formVehiculo(forms.Form):
    tipoV = forms.CharField()
    marcaV = forms.CharField()
    modeloV = forms.CharField()
    ruedas = forms.IntegerField()
    #email = forms.EmailField()
    fecha_produccionV = forms.DateField() #(YYYY-MM-DD)

class BusquedaFamiliar(forms.Form):
    nombre = forms.CharField()


