from django.shortcuts import render,get_object_or_404,redirect
#---->Importamos el Sector de Formularios
from .forms import *
from .models import *
#--->Importamos la Libreria de Logout
from django.contrib.auth import logout
#--->Importamos la Libreria de Permisos
from django.contrib.auth.decorators import login_required, permission_required
from django.db.models import Q

#--->Libreria para mensajes
from django.contrib import messages

# Create your views here.
def Home(request):
    buscar=Personajes.objects.all().order_by('-Codigo')[:3]
    data={
        'forms':buscar
    }
    return render (request,'index.html',data)

from django.db.models import Q

def ver_Personajes(request):
    #--->TREAMOS TODOS LOS ELEMENTOS DEL TABLA
    buscar=Personajes.objects.all()
    filtro=request.GET.get('filtro')

    if filtro:
        buscar=Personajes.objects.filter(
            Q(Nombre__icontains=filtro)
        ).distinct()
    else:
        buscar=Personajes.objects.all()
    data={
        'forms':buscar
    }
    return render(request,'Pages/visualizar.html',data)

def ver_mas(request,Codigo):
    buscar=Personajes.objects.filter(Codigo=Codigo)
    data={
        'forms':buscar
    }
    return render(request,'Pages/ver_mas.html',data)

#--->Libreria para mensajes
from django.contrib import messages
@login_required

@permission_required('App.add_personajes')
def Agregar(request):
    data={
        'forms':NuevoPersonaje()
    }
    if request.method=='POST':
        query=NuevoPersonaje(data=request.POST,files=request.FILES)
        if  query.is_valid():
            query.save()
            messages.success(request,"Datos Registrados")
        else:
            data['forms']=NuevoPersonaje
    return render (request,'Pages/agregar.html',data)


@permission_required('App.change_personajes')
def Modificar_Personajes(request,Codigo):
    sql=get_object_or_404(Personajes,Codigo=Codigo)
    data={
        'forms':NuevoPersonaje(instance=sql)
    }
    if request.method=='POST':
        query=NuevoPersonaje(data=request.POST,instance=sql,files=request.FILES)
        if  query.is_valid():
            query.save()
            messages.success(request,"Registrado Correctamente")
        else:
            data['forms']=NuevoPersonaje
    return render (request,'Pages/modificar.html',data)


@permission_required('App.delete_personajes')
def Eliminar_Personajes(request,Codigo):
    buscar=get_object_or_404(Personajes,Codigo=Codigo)
    buscar.delete()
    return redirect(to="visualizar")


def salir(request):
    logout(request)
    return redirect(to='inicio')