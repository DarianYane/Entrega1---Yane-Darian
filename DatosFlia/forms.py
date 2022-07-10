from django import forms

class formFamiliar(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    dni = forms.IntegerField()
    email = forms.EmailField()
    fecha_nacimiento = forms.DateField() #(YYYY-MM-DD)

class BusquedaFamiliar(forms.Form):
    nombre = forms.CharField()


