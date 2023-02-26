from django.shortcuts import render,redirect
from django.core import serializers
from apps.pqrs.models import Categoria,Tipospq,Lista, opciones_Presentaciones, opciones_Productos # opciones_horaFin

from django.http import JsonResponse

# from django.contrib.auth.views import LoginView,LogoutView
import core.settings as setting
import json



def tipospqs(request):
    listaTipospqs = Tipospq.objects.all()
    return render(request, 'tipospqs.html',{'tipospqs': listaTipospqs})


def detalleTipospq(request,id):
    vertipospq = Tipospq.objects.get(id=id)
    listaCategorias = Categoria.objects.all()
    listaListas=Lista.objects.all()
   
    data = {'horarioI':opciones_Presentaciones, 'horarioF':opciones_Productos,'verTipospq':vertipospq, 'categorias': listaCategorias,'listas':listaListas}
    return render(request, 'vista_categoria.html',data)

def categoria2(request):
    busqueda= request.GET.get("buscarcategoria")
    listaCategorias = Categoria.objects.all()

    if busqueda:
        listaCategorias=Categoria.objects.filter(
            nombre__icontains=busqueda 
        ).distinct()
    return render(request, 'categoria2.html',{'categorias': listaCategorias})

def registroCategoria(request):
    nombre = request.POST['disnombre']

    Categoria.objects.create(
        nombre=nombre,
    )
    return redirect('/categoria2')

def editaCategoria(request,id):
    edicioncategoria = Categoria.objects.get(id=id)
    return render(request, 'edicionCategorias.html', {'edicionCategoria': edicioncategoria})

def edicionCategorias(request):
    id=request.POST['categoriaid']
    categoria = Categoria.objects.get(id=id)

    if request.POST:
        categoria=Categoria()
        categoria.id = request.POST.get('categoriaid')
        categoria.nombre = request.POST.get('categorianombre')
        categoria.save()
    return redirect('/categoria2')

def eliminacionCategoria(request,id):
    categoria=Categoria.objects.get(id=id)
    categoria.delete()
    
    return redirect('/categoria2')    

def categoria1(request):
    listaCategorias = Categoria.objects.all()
    listaTipospqs = Tipospq.objects.all()
    busqueda= request.GET.get("buscartipospq")

    if busqueda:
        listaTipospqs=Tipospq.objects.filter(
            nombre__icontains=busqueda 
        ).distinct()

    return render(request, 'categoria1.html',{'categorias': listaCategorias,'tipospqs': listaTipospqs})

def registroTipospq(request):
    nombre = request.POST['nombre']

    categoria=Categoria()
    categoria.id = int(request.POST['categoria'])
    categoria_tipospq=categoria

    #precio = request.POST['precio']
    #capacidad = request.POST['capacidad']
    foto = request.FILES['imagen']
    descripcion = request.POST['descripcion']
    #indumentaria = request.POST['indumentaria']
    #recomendaciones = request.POST['recomendaciones']
    restricciones = request.POST['restricciones']
    #equipo_incluido = request.POST['equipo_incluido']
    

    Tipospq.objects.create(
        nombre=nombre,
        id_diciplina=categoria_tipospq,
        descripcion=descripcion,
        restriciones=restricciones,
        #precio=precio,
        #capacidad=capacidad,
        imagen=foto,
        #indumentaria=indumentaria,
        #recomendaciones=recomendaciones,
        #equipo_incluido=equipo_incluido,
    )
    return redirect('/categoria1')


def verTipospq(request,id):
    vertipospq = Tipospq.objects.get(id=id)
    listaCategorias = Categoria.objects.all()
    listaListas=Lista.objects.all()
   
    data = {'horarioI':opciones_Presentaciones, 'horarioF':opciones_Productos, 'verTipospq':vertipospq,'categorias': listaCategorias,'listas':listaListas}
    
    return render(request, 'verCategorias.html',  data)

def editaTipospq(request,id):
    ediciontipospq = Tipospq.objects.get(id=id)
    imagen=ediciontipospq.imagen
    if request.POST:
        if request.POST.get('imagen')=='':
            tipospq=Tipospq()
            tipospq.id = ediciontipospq.id
            tipospq.nombre=request.POST.get('nombre')
            
            categoria=Categoria()
            categoria.id=request.POST.get('categoria')
            tipospq.id_categoria=categoria

            #instalacion.precio=request.POST.get('precio')
            #instalacion.capacidad=request.POST.get('capacidad')
            tipospq.imagen=imagen
            tipospq.descripcion=request.POST.get('descripcion')
            #instalacion.indumentaria=request.POST.get('indumentaria')
            #instalacion.recomendaciones=request.POST.get('recomendaciones')
            tipospq.restriciones=request.POST.get('restricciones')
            #instalacion.equipo_incluido=request.POST.get('equipo_incluido')

            tipospq.save()
        else:
            tipospq=Tipospq()
            tipospq.id = ediciontipospq.id
            tipospq.nombre=request.POST.get('nombre')
            
            categoria=Categoria()
            categoria.id=request.POST.get('categoria')
            tipospq.id_categoria=categoria

           # instalacion.precio=request.POST.get('precio')
            #instalacion.capacidad=request.POST.get('capacidad')
            tipospq.imagen=request.FILES.get('imagen')
            #instalacion.descripcion=request.POST.get('descripcion')
            #instalacion.indumentaria=request.POST.get('indumentaria')
            tipospq.recomendaciones=request.POST.get('recomendaciones')
            tipospq.restriciones=request.POST.get('restricciones')
            #instalacion.equipo_incluido=request.POST.get('equipo_incluido')

            tipospq.save()

    return redirect('/verCategoria/'+str(tipospq.id))

def eliminacionTipospq(request,id):
    tipospq=Tipospq.objects.get(id=id)
    tipospq.delete()
    
    return redirect('/categorias1') 

def about(request):
    listaLista = Lista.objects.all()
    # lo transforma en json
    serialized_data = serializers.serialize('json', listaLista)
    deserialized_data = json.loads(serialized_data)
    # fields son los datos que limpiamos de la base de datos
    listaNueva = [_["fields"] for _ in deserialized_data]
    listaForm = [];
    # creamos una list con los dos arrays
    for d in listaNueva:
        for pre, pro in zip(opciones_Presentaciones, opciones_Productos):
            if d["Presentaciones"] == pre[0]:
                d["Presentaciones"] =  pre[1]

            if d["Productos"] == pro[0]:
                d["Productos"] =  pro[1]
        listaForm.append(d)
    # cambiamos  reservas con el nuevo json  listaFrom    
    data = {'horarioI':opciones_Presentaciones, 'horarioF':opciones_Productos, 'listas':listaForm}
    return render(request, 'about.html', data)

def registroListas(request,id):
    nombre = request.POST['nombre']
    apellido = request.POST['apellido']
    ci = request.POST['ci']
    telefono = request.POST['telefono']
    correo = request.POST['correo']

    tipospq=Tipospq()
    tipospq.id = int(id)
    tipospq_lista=tipospq

    # codigo=str(request.POST['apellido'])+str(request.POST['ci'])+str(request.POST['telefono']) 
    cantidad = request.POST['cantidad']

    fecha_lista = request.POST['fecha_lista']
    Presentaciones = request.POST['Presentaciones']
    Productos = request.POST['Productos']
    

    Lista.objects.create(
        nombres=nombre,
        apellidos=apellido,
        cedula=ci,
        telefono=telefono,
        email=correo,
        id_tipospq=tipospq_lista,
        fecha_compra=fecha_lista,
        # codigo_qr=codigo,
        cantidad=cantidad,
        Presentaciones=Presentaciones,
        Productos=Productos,

        
    )
    
    return redirect('/tipospqs')



def validarFecha(request):
    fecha = request.GET.get('fecha_Lista', None)
    data = {
        'is_taken': Lista.objects.filter(fecha_compra=fecha).exists()
    }
    
    return JsonResponse(data)
