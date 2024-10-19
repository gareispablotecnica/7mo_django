#--->Importamos 'FORMS'
from django import forms
#---> Importamos los Modelos/Tablas
from .models import *

#---> validaciones
from django.forms import ValidationError

class NuevoPersonaje(forms.ModelForm):

    def verificaciones(self):
        Codigo=self.cleaned_data['Codigo']
        validacion=Personajes.objects.filter(Codigo=Codigo).exists()

        if validacion:
            raise ValidationError("Codigo ya Registrado")
    
    class Meta:
        model=Personajes
        fields='__all__'