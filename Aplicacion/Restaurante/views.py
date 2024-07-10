from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
from django.db.models.deletion import ProtectedError
from .forms import *
from django.http import HttpResponse
from datetime import datetime


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    next_url = request.GET.get('next', 'bienvenida')
                    return redirect(next_url)
                else:
                    return HttpResponse('El Usuario no está activo')
            else:
                return HttpResponse('La información no es correcta')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})
#########################################################################################################################




def plantillaCliente(request):
    return render(request, 'plantillaCliente.html')

def menus(request):
    return render(request, 'menus.html')

def listadoOrdenMenus(request):
    menuBdd = Menus.objects.all()
    return render(request, 'listadoOrdenMenus.html',{'menus': menuBdd})



#################################################################################################################################
def bienvenida(request):
    clienteBdd = Clientes.objects.all()
    return render(request, 'bienvenida.html',{'clientes': clienteBdd})


def listadoClientes(request):
    clienteBdd = Clientes.objects.all()
    return render(request, 'listadoClientes.html',{'clientes': clienteBdd})

def guardarClientes(request):
    nombre_cli = request.POST["nombre_cli"]
    apellido_cli = request.POST["apellido_cli"]
    email_cli = request.POST["email_cli"]
    telefono_cli = request.POST["telefono_cli"]
    cedula_cli = request.POST["cedula_cli"]
    fecha_Reguistro_cli = request.POST["fecha_Reguistro_cli"]
    nuevoClientes = Clientes.objects.create(nombre_cli=nombre_cli, apellido_cli=apellido_cli, cedula_cli=cedula_cli,
                                             email_cli=email_cli, telefono_cli=telefono_cli,
                                             fecha_Reguistro_cli=fecha_Reguistro_cli)
    messages.success(request, '¡Cliente guardado exitosamente!')
    return redirect('listadoClientes')


def eliminarClientes(request, cliente_id):
    try:
        cliente = Clientes.objects.get(pk=cliente_id)
        cliente.delete()
        messages.success(request, 'Cliente eliminado correctamente.')
    except Clientes.DoesNotExist:
        messages.error(request, 'El Cliente que intentas eliminar no existe.')
    except ProtectedError:
        messages.error(request, 'No se puede eliminar el cliente porque es un cliente con registro.')
    return redirect('listadoClientes')


def editarClientes(request, cliente_id):
    clienteEditar = Clientes.objects.get(cliente_id=cliente_id)
    return render(request, 'editarClientes.html', {'clientes': clienteEditar})

def procesarActualizacionClientes(request):
    cliente_id = request.POST["cliente_id"]
    nombre_cli = request.POST["nombre_cli"]
    apellido_cli = request.POST["apellido_cli"]
    email_cli = request.POST["email_cli"]
    telefono_cli = request.POST["telefono_cli"]
    cedula_cli = request.POST["cedula_cli"]
    fecha_Reguistro_cli = request.POST["fecha_Reguistro_cli"]
    # Insertando datos mediante el ORM de DJANGO
    clienteEditar = Clientes.objects.get(cliente_id=cliente_id)
    clienteEditar.nombre_cli = nombre_cli
    clienteEditar.apellido_cli = apellido_cli
    clienteEditar.email_cli = email_cli
    clienteEditar.telefono_cli = telefono_cli
    clienteEditar.cedula_cli = cedula_cli
    clienteEditar.fecha_Reguistro_cli = fecha_Reguistro_cli
    clienteEditar.save()
    messages.success(request, 'Cliente ACTUALIZADO Exitosamente')
    return redirect('listadoClientes')

#########################################################################################################################

def listadoMesas(request):
    mesaBdd = Mesas.objects.all()
    return render(request, 'listadoMesas.html', {'mesas': mesaBdd})


def guardarMesas(request):
    numero_mes = request.POST["numero_mes"]
    capacidad_mes = request.POST["capacidad_mes"]
    estado_mes = request.POST["estado_mes"]
    nuevoMesas = Mesas.objects.create(numero_mes=numero_mes, capacidad_mes=capacidad_mes, estado_mes=estado_mes)
    messages.success(request, '¡Mesa guardado exitosamente!')
    return redirect('listadoMesas')

def eliminarMesas(request, id_mesa):
    try:
        mesa = Mesas.objects.get(pk=id_mesa)
        mesa.delete()
        messages.success(request, 'Mesa eliminado correctamente.')
    except Mesas.DoesNotExist:
        messages.error(request, 'La Mesa que intentas eliminar no existe.')
    except ProtectedError:
        messages.error(request, 'No se puede eliminar la Mesa por motivos de Datos.')
    return redirect('listadoMesas')

def editarMesas(request, id_mesa):
    mesaEditar = Mesas.objects.get(id_mesa=id_mesa)
    return render(request, 'editarMesas.html', {'mesas': mesaEditar})


def procesarActualizacionMesas(request):
    id_mesa = request.POST["id_mesa"]
    numero_mes = request.POST["numero_mes"]
    capacidad_mes = request.POST["capacidad_mes"]
    estado_mes = request.POST["estado_mes"]
    # Insertando datos mediante el ORM de DJANGO
    mesaEditar = Mesas.objects.get(id_mesa=id_mesa)
    mesaEditar.numero_mes = numero_mes
    mesaEditar.capacidad_mes = capacidad_mes
    mesaEditar.estado_mes = estado_mes
    mesaEditar.save()
    messages.success(request, 'Mesa Actualizado Exitosamente')
    return redirect('listadoMesas')
#############################################################################################################################################
def listadoReservas(request):
    clienteBdd = Clientes.objects.all()
    mesaBdd = Mesas.objects.all()
    reservaBdd = Reservas.objects.all()
    return render(request, 'listadoReservas.html', {'reservas': reservaBdd,'clientes':clienteBdd,'mesas':mesaBdd })


def guardarReservas(request):
    cliente_id_cliente=request.POST["cliente_id_cliente"]
    clienteSeleccionado=Clientes.objects.get(cliente_id=cliente_id_cliente)
    id_mesa_mesa=request.POST["id_mesa_mesa"]
    mesaSeleccionado=Mesas.objects.get(id_mesa=id_mesa_mesa)
    fecha_reserva=request.POST["fecha_reserva"]
    hora_reserva = request.POST.get('hora_reserva', None)
    numero_personas_reserva=request.POST["numero_personas_reserva"]
    estado_reserva=request.POST["estado_reserva"]

    nuevoReservas = Reservas.objects.create(
        fecha_reserva=fecha_reserva,
        hora_reserva=hora_reserva,
        numero_personas_reserva=numero_personas_reserva,
        estado_reserva=estado_reserva,
        mesa=mesaSeleccionado,
        cliente=clienteSeleccionado
    )

    messages.success(request, 'Reserva guardada exitosamente')
    return redirect('listadoReservas')


def eliminarReservas(request, reserva_id):
    try:
        reserva = Reservas.objects.get(pk=reserva_id)
        reserva.delete()
        messages.success(request, 'Reserva eliminado correctamente.')
    except Reservas.DoesNotExist:
        messages.error(request, 'La Reserva que intentas eliminar no existe.')
    except ProtectedError:
        messages.error(request, 'No se puede eliminar la Reserva porque hay productos relacionados.')
    return redirect('listadoReservas')

def editarReservas(request,reserva_id):
    reservaEditar=Reservas.objects.get(reserva_id=reserva_id)
    mesaBdd = Mesas.objects.all()
    clienteBdd = Clientes.objects.all()
    return render(request, 'editarReservas.html', {'reservas': reservaEditar,'clientes':clienteBdd,'mesas':mesaBdd })

def procesarActualizacionReservas(request):
    reserva_id=request.POST["reserva_id"]
    cliente_id_cliente=request.POST["cliente_id_cliente"]
    clienteSeleccionado=Clientes.objects.get(cliente_id=cliente_id_cliente)
    id_mesa_mesa=request.POST["id_mesa_mesa"]
    mesaSeleccionado=Mesas.objects.get(id_mesa=id_mesa_mesa)
    fecha_reserva=request.POST["fecha_reserva"]
    hora_reserva = request.POST.get('hora_reserva', None)
    numero_personas_reserva=request.POST["numero_personas_reserva"]
    estado_reserva=request.POST["estado_reserva"]
    #Insertando datos mediante el ORM de DJANGO
    reservaEditar=Reservas.objects.get(reserva_id=reserva_id)
    reservaEditar.cliente=clienteSeleccionado
    reservaEditar.mesa=mesaSeleccionado
    reservaEditar.fecha_reserva=fecha_reserva
    reservaEditar.hora_reserva=hora_reserva
    reservaEditar.numero_personas_reserva=numero_personas_reserva
    reservaEditar.estado_reserva=estado_reserva
    reservaEditar.save()
    messages.success(request,
      'Reserva ACTUALIZADO Exitosamente')
    return redirect('listadoReservas')

#############################################################################################################################################
def listadoVentas(request):
    clienteBdd = Clientes.objects.all()
    ventaBdd = Ventas.objects.all()
    return render(request, 'listadoVentas.html', {'ventas': ventaBdd,'clientes':clienteBdd})



def guardarVentas(request):
    cliente_id_cliente=request.POST["cliente_id_cliente"]
    clienteSeleccionado=Clientes.objects.get(cliente_id=cliente_id_cliente)
    fecha_venta=request.POST["fecha_venta"]
    total_venta=request.POST["total_venta"]

    nuevoVentas = Ventas.objects.create(
        fecha_venta=fecha_venta,
        total_venta=total_venta,
        cliente=clienteSeleccionado
    )

    messages.success(request, 'Venta guardada exitosamente')
    return redirect('listadoVentas')


def eliminarVentas(request, venta_id):
    try:
        venta = Ventas.objects.get(pk=venta_id)
        venta.delete()
        messages.success(request, 'Ventas eliminado correctamente.')
    except Reservas.DoesNotExist:
        messages.error(request, 'Las Ventas que intentas eliminar no existe.')
    except ProtectedError:
        messages.error(request, 'No se puede eliminar la Reserva porque hay Cliente relacionados.')
    return redirect('listadoVentas')

def editarVentas(request,venta_id):
    ventaEditar=Ventas.objects.get(venta_id=venta_id)
    clienteBdd = Clientes.objects.all()
    return render(request, 'editarVentas.html', {'ventas': ventaEditar,'clientes':clienteBdd})

def procesarActualizacionVentas(request):
    venta_id=request.POST["venta_id"]
    cliente_id_cliente=request.POST["cliente_id_cliente"]
    clienteSeleccionado=Clientes.objects.get(cliente_id=cliente_id_cliente)
    fecha_venta=request.POST["fecha_venta"]
    total_venta=request.POST["total_venta"]
    #Insertando datos mediante el ORM de DJANGO
    ventaEditar=Ventas.objects.get(venta_id=venta_id)
    ventaEditar.cliente=clienteSeleccionado
    ventaEditar.fecha_venta=fecha_venta
    ventaEditar.total_venta=total_venta
    ventaEditar.save()
    messages.success(request,
      'Venta ACTUALIZADO Exitosamente')
    return redirect('listadoVentas')
##################################################################################################################################################
def listadoMenus(request):
    menuBdd = Menus.objects.all()
    return render(request, 'listadoMenus.html',{'menus': menuBdd})

def guardarMenus(request):
    nombre_menu = request.POST["nombre_menu"]
    descripcion_menu = request.POST["descripcion_menu"]
    categoria_menu = request.POST["categoria_menu"]
    disponibilidad_menu = request.POST["disponibilidad_menu"]
    precio_menu = request.POST["precio_menu"]
    fotos_menu = request.FILES.get("fotos_menu")

    nuevoMenu = Menus.objects.create(
        nombre_menu=nombre_menu,
        descripcion_menu=descripcion_menu,
        categoria_menu=categoria_menu,
        disponibilidad_menu=disponibilidad_menu,
        precio_menu=precio_menu,
        fotos_menu=fotos_menu
    )
    messages.success(request, 'Menú guardado exitosamente')
    return redirect('listadoMenus')



def eliminarMenus(request, menu_id):
    try:
        menu = Menus.objects.get(pk=menu_id)
        menu.delete()
        messages.success(request, 'Menus eliminado correctamente.')
    except Menus.DoesNotExist:
        messages.error(request, 'El Menu que intentas eliminar no existe.')
    except ProtectedError:
        messages.error(request, 'No se puede eliminar el menu porque es un cliente con registro.')
    return redirect('listadoMenus')


def editarMenus(request, menu_id):
    menuEditar = Menus.objects.get(menu_id=menu_id)
    return render(request, 'editarMenus.html', {'menus': menuEditar})

def procesarActualizacionMenus(request):
    menu_id = request.POST["menu_id"]
    nombre_menu = request.POST["nombre_menu"]
    descripcion_menu = request.POST["descripcion_menu"]
    categoria_menu = request.POST["categoria_menu"]
    disponibilidad_menu = request.POST["disponibilidad_menu"]
    precio_menu = request.POST["precio_menu"]
    fotos_menu=request.FILES.get("fotos_menu")
    # Insertando datos mediante el ORM de DJANGO
    menuEditar = Menus.objects.get(menu_id=menu_id)
    menuEditar.nombre_menu = nombre_menu
    menuEditar.descripcion_menu = descripcion_menu
    menuEditar.categoria_menu = categoria_menu
    menuEditar.disponibilidad_menu = disponibilidad_menu
    menuEditar.precio_menu = precio_menu
    menuEditar.fotos_menu = fotos_menu
    menuEditar.save()
    messages.success(request, 'Menu ACTUALIZADO Exitosamente')
    return redirect('listadoMenus')

#############################################################################################################################################

def listadoDetalles_Ventas(request):
    detalleBdd = Detalles_Ventas.objects.all()
    ventaBdd = Ventas.objects.all()
    menuBdd = Menus.objects.all()
    return render(request, 'listadoDetalles_Ventas.html', {'detalles': detalleBdd, 'ventas': ventaBdd, 'menus': menuBdd})

def guardarDetalles_Ventas(request):
    venta_id_venta=request.POST["venta_id_venta"]
    ventaSeleccionado=Ventas.objects.get(venta_id=venta_id_venta)
    menu_id_menu=request.POST["menu_id_menu"]
    menuSeleccionado=Menus.objects.get(menu_id=menu_id_menu)
    cantidad_venta=request.POST["cantidad_venta"]
    precio_unitario_venta=request.POST["precio_unitario_venta"]

    nuevodetalle = Detalles_Ventas.objects.create(
        cantidad_venta=cantidad_venta,
        precio_unitario_venta=precio_unitario_venta,
        venta=ventaSeleccionado,
        menu=menuSeleccionado
    )

    messages.success(request, 'Detalles Reservas guardada exitosamente')
    return redirect('listadoDetalles_Ventas')


def eliminarDetalles_Ventas(request, detalle_venta_id):
    try:
        detalles = Detalles_Ventas.objects.get(pk=detalle_venta_id)
        detalles.delete()
        messages.success(request, 'Detalles Ventas eliminado correctamente.')
    except Detalles_Ventas.DoesNotExist:
        messages.error(request, 'Los Detalles Ventas que intentas eliminar no existe.')
    except ProtectedError:
        messages.error(request, 'No se puede eliminar el Detalles Ventas porque hay productos relacionados.')
    return redirect('listadoDetalles_Ventas')

def editarDetalles_Ventas(request,detalle_venta_id):
    detalleEditar=Detalles_Ventas.objects.get(detalle_venta_id=detalle_venta_id)
    ventaBdd = Ventas.objects.all()
    menuBdd = Menus.objects.all()
    return render(request, 'editarDetalles_Ventas.html', {'detalles': detalleEditar,'ventas':ventaBdd,'menus':menuBdd })

def procesarActualizacionDetalles(request):
    detalle_venta_id=request.POST["detalle_venta_id"]
    venta_id_venta=request.POST["venta_id_venta"]
    ventaSeleccionado=Ventas.objects.get(venta_id=venta_id_venta)
    menu_id_menu=request.POST["menu_id_menu"]
    menuSeleccionado=Menus.objects.get(menu_id=menu_id_menu)
    cantidad_venta=request.POST["cantidad_venta"]
    precio_unitario_venta=request.POST["precio_unitario_venta"]
    #Insertando datos mediante el ORM de DJANGO
    detalleEditar=Detalles_Ventas.objects.get(detalle_venta_id=detalle_venta_id)
    detalleEditar.menu=menuSeleccionado
    detalleEditar.venta=ventaSeleccionado
    detalleEditar.cantidad_venta=cantidad_venta
    detalleEditar.precio_unitario_venta=precio_unitario_venta
    detalleEditar.save()
    messages.success(request,
      'Detalles Ventas ACTUALIZADO Exitosamente')
    return redirect('listadoDetalles_Ventas')

#############################################################################################################################
def listadoDetalles_Reservas(request):
    detalle_ReservaBdd = Detalles_Reservas.objects.all()
    reservaBdd = Reservas.objects.all()
    menuBdd = Menus.objects.all()
    return render(request, 'listadoDetalles_Reservas.html', {'detalle_Reservas': detalle_ReservaBdd, 'reservas': reservaBdd, 'menus': menuBdd})

def guardarDetalles_Reservas(request):
    reserva_id_reserva=request.POST["reserva_id_reserva"]
    reservaSeleccionado=Reservas.objects.get(reserva_id=reserva_id_reserva)
    menu_id_menu=request.POST["menu_id_menu"]
    menuSeleccionado=Menus.objects.get(menu_id=menu_id_menu)


    nuevodetalle_Reserva = Detalles_Reservas.objects.create(
        reserva=reservaSeleccionado,
        menu=menuSeleccionado
    )

    messages.success(request, 'Detalles Reservas guardada exitosamente')
    return redirect('listadoDetalles_Reservas')


def eliminarDetalles_Reservas(request, detalle_reserva_id):
    try:
        detalles_Reservas = Detalles_Reservas.objects.get(pk=detalle_reserva_id)
        detalles_Reservas.delete()
        messages.success(request, 'Detalles Ventas eliminado correctamente.')
    except Detalles_Reservas.DoesNotExist:
        messages.error(request, 'Los Detalles Ventas que intentas eliminar no existe.')
    except ProtectedError:
        messages.error(request, 'No se puede eliminar el Detalles Ventas porque hay productos relacionados.')
    return redirect('listadoDetalles_Reservas')

def editarDetalles_Reservas(request,detalle_reserva_id):
    detalle_ReservaEditar=Detalles_Reservas.objects.get(detalle_reserva_id=detalle_reserva_id)
    reservaBdd = Reservas.objects.all()
    menuBdd = Menus.objects.all()
    return render(request, 'editarDetalles_Reservas.html', {'detalle_Reservas': detalle_ReservaEditar,'reservas':reservaBdd,'menus':menuBdd })

def procesarActualizacionDetalles_Reservas(request):
    detalle_reserva_id=request.POST["detalle_reserva_id"]
    reserva_id_reserva=request.POST["reserva_id_reserva"]
    reservaSeleccionado=Reservas.objects.get(reserva_id=reserva_id_reserva)
    menu_id_menu=request.POST["menu_id_menu"]
    menuSeleccionado=Menus.objects.get(menu_id=menu_id_menu)

    detalle_ReservaEditar=Detalles_Reservas.objects.get(detalle_reserva_id=detalle_reserva_id)
    detalle_ReservaEditar.menu=menuSeleccionado
    detalle_ReservaEditar.reserva=reservaSeleccionado
    detalle_ReservaEditar.save()
    messages.success(request,
      'Detalles Ventas ACTUALIZADO Exitosamente')
    return redirect('listadoDetalles_Reservas')
########################################################################################################################################################

def listadoPromociones(request):
    promocionBdd = Promociones.objects.all()
    menuBdd = Menus.objects.all()
    return render(request, 'listadoPromociones.html', {'promociones': promocionBdd,'menus':menuBdd})


def guardarPromociones(request):
    menu_id_menu=request.POST["menu_id_menu"]
    menuSeleccionado=Menus.objects.get(menu_id=menu_id_menu)
    descripcion_pro=request.POST["descripcion_pro"]
    fecha_inicio_pro = request.POST.get('fecha_inicio_pro')
    fecha_fin_pro = request.POST.get('fecha_fin_pro')
    descuento_pro=request.POST["descuento_pro"]

    nuevoPromociones = Promociones.objects.create(
        descripcion_pro=descripcion_pro,
        fecha_inicio_pro=fecha_inicio_pro,
        fecha_fin_pro=fecha_fin_pro,
        descuento_pro=descuento_pro,
        menu=menuSeleccionado
    )

    messages.success(request, 'Promociones guardada exitosamente')
    return redirect('listadoPromociones')


def eliminarPromociones(request, promociones_id):
    try:
        promocion = Promociones.objects.get(pk=promociones_id)
        promocion.delete()
        messages.success(request, 'Promocion eliminado correctamente.')
    except Reservas.DoesNotExist:
        messages.error(request, 'La Promocion que intentas eliminar no existe.')
    except ProtectedError:
        messages.error(request, 'No se puede eliminar la Promocion porque hay productos relacionados.')
    return redirect('listadoPromociones')

def editarPromociones(request,promociones_id):
    promocionEditar=Promociones.objects.get(promociones_id=promociones_id)
    menuBdd = Menus.objects.all()
    return render(request, 'editarPromociones.html', {'promociones': promocionEditar,'menus':menuBdd})

def procesarActualizacionPromociones(request):
    promociones_id=request.POST["promociones_id"]
    menu_id_menu=request.POST["menu_id_menu"]
    menuSeleccionado=Menus.objects.get(menu_id=menu_id_menu)
    descripcion_pro=request.POST["descripcion_pro"]
    fecha_inicio_pro = request.POST.get('fecha_inicio_pro')
    fecha_fin_pro = request.POST.get('fecha_fin_pro')
    descuento_pro=request.POST["descuento_pro"]
    #Insertando datos mediante el ORM de DJANGO
    promocionEditar=Promociones.objects.get(promociones_id=promociones_id)
    promocionEditar.menu=menuSeleccionado
    promocionEditar.descripcion_pro=descripcion_pro
    promocionEditar.fecha_inicio_pro=fecha_inicio_pro
    promocionEditar.fecha_fin_pro=fecha_fin_pro
    promocionEditar.descuento_pro=descuento_pro
    promocionEditar.save()
    messages.success(request,
      'Procion ACTUALIZADO Exitosamente')
    return redirect('listadoPromociones')
