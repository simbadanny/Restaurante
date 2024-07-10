from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views

urlpatterns = [
    path('', views.plantillaCliente, name='plantillaCliente'),

    path('bienvenida/', login_required(views.bienvenida), name='bienvenida'),

    path('listadoOrdenMenus/',views.listadoOrdenMenus, name='listadoOrdenMenus'),

    path('listadoClientes/', login_required(views.listadoClientes), name='listadoClientes'),
    path('guardarClientes/', login_required(views.guardarClientes), name='guardarClientes'),
    path('eliminarClientes/<int:cliente_id>/', login_required(views.eliminarClientes), name='eliminarClientes'),
    path('editarClientes/<int:cliente_id>/', login_required(views.editarClientes), name='editarClientes'),
    path('procesarActualizacionClientes/', login_required(views.procesarActualizacionClientes), name='procesarActualizacionClientes'),

    path('listadoMesas/', login_required(views.listadoMesas), name='listadoMesas'),
    path('guardarMesas/', login_required(views.guardarMesas), name='guardarMesas'),
    path('eliminarMesas/<int:id_mesa>/', login_required(views.eliminarMesas), name='eliminarMesas'),
    path('editarMesas/<int:id_mesa>/', login_required(views.editarMesas), name='editarMesas'),
    path('procesarActualizacionMesas/', login_required(views.procesarActualizacionMesas), name='procesarActualizacionMesas'),

    path('listadoReservas/', login_required(views.listadoReservas), name='listadoReservas'),
    path('guardarReservas/', login_required(views.guardarReservas), name='guardarReservas'),
    path('eliminarReservas/<int:reserva_id>/', login_required(views.eliminarReservas), name='eliminarReservas'),
    path('editarReservas/<int:reserva_id>/', login_required(views.editarReservas), name='editarReservas'),
    path('procesarActualizacionReservas/', login_required(views.procesarActualizacionReservas), name='procesarActualizacionReservas'),

    path('listadoVentas/', login_required(views.listadoVentas), name='listadoVentas'),
    path('guardarVentas/', login_required(views.guardarVentas), name='guardarVentas'),
    path('eliminarVentas/<int:venta_id>/', login_required(views.eliminarVentas), name='eliminarVentas'),
    path('editarVentas/<int:venta_id>/', login_required(views.editarVentas), name='editarVentas'),
    path('procesarActualizacionVentas/', login_required(views.procesarActualizacionVentas), name='procesarActualizacionVentas'),

    path('listadoMenus/', login_required(views.listadoMenus), name='listadoMenus'),
    path('guardarMenus/', login_required(views.guardarMenus), name='guardarMenus'),
    path('eliminarMenus/<int:menu_id>/', login_required(views.eliminarMenus), name='eliminarMenus'),
    path('editarMenus/<int:menu_id>/', login_required(views.editarMenus), name='editarMenus'),
    path('procesarActualizacionMenus/', login_required(views.procesarActualizacionMenus), name='procesarActualizacionMenus'),

    path('listadoDetalles_Ventas/', login_required(views.listadoDetalles_Ventas), name='listadoDetalles_Ventas'),
    path('guardarDetalles_Ventas/', login_required(views.guardarDetalles_Ventas), name='guardarDetalles_Ventas'),
    path('eliminarDetalles_Ventas/<int:detalle_venta_id>/', login_required(views.eliminarDetalles_Ventas), name='eliminarDetalles_Ventas'),
    path('editarDetalles_Ventas/<int:detalle_venta_id>/', login_required(views.editarDetalles_Ventas), name='editarDetalles_Ventas'),
    path('procesarActualizacionDetalles/', login_required(views.procesarActualizacionDetalles), name='procesarActualizacionDetalles'),

    path('listadoDetalles_Reservas/', login_required(views.listadoDetalles_Reservas), name='listadoDetalles_Reservas'),
    path('guardarDetalles_Reservas/', login_required(views.guardarDetalles_Reservas), name='guardarDetalles_Reservas'),
    path('eliminarDetalles_Reservas/<int:detalle_reserva_id>/', login_required(views.eliminarDetalles_Reservas), name='eliminarDetalles_Reservas'),
    path('editarDetalles_Reservas/<int:detalle_reserva_id>/', login_required(views.editarDetalles_Reservas), name='editarDetalles_Reservas'),
    path('procesarActualizacionDetalles_Reservas/', login_required(views.procesarActualizacionDetalles_Reservas), name='procesarActualizacionDetalles_Reservas'),

    path('listadoPromociones/', login_required(views.listadoPromociones), name='listadoPromociones'),
    path('guardarPromociones/', login_required(views.guardarPromociones), name='guardarPromociones'),
    path('eliminarPromociones/<int:promociones_id>/', login_required(views.eliminarPromociones), name='eliminarPromociones'),
    path('editarPromociones/<int:promociones_id>/', login_required(views.editarPromociones), name='editarPromociones'),
    path('procesarActualizacionPromociones/', login_required(views.procesarActualizacionPromociones), name='procesarActualizacionPromociones'),

]
