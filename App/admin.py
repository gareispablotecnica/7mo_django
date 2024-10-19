from django.contrib import admin
#--->Traemos la Tablas desde MODELS
from .models import *
#--->Traemos los Formularios Generados
from .forms import *

class AdminImagenes(admin.TabularInline):
    model=ImagenPersonajes

class AdminPersonajes(admin.ModelAdmin):
    forms=NuevoPersonaje
    inlines=[
        AdminImagenes
    ]

# Register your models here.
admin.site.register(Personajes,AdminPersonajes)