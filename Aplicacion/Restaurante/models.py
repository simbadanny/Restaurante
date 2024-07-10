from django.db import models



# Relaciones Clientes esta relaciona de 1 a muchos a reservas y ventas
class Clientes(models.Model):
    cliente_id = models.AutoField(primary_key=True)
    nombre_cli = models.CharField(max_length=50)
    apellido_cli = models.CharField(max_length=150)
    email_cli = models.EmailField()
    cedula_cli = models.CharField(max_length=10, null=True, blank=True)
    telefono_cli = models.CharField(max_length=15)
    fecha_Reguistro_cli = models.DateField()


    def __str__(self):
        fila="{0}: {1}"
        return fila.format(self.cliente_id,self.nombre_cli)


class Mesas(models.Model):
    id_mesa = models.AutoField(primary_key=True)
    numero_mes = models.CharField(max_length=50, null=True, blank=True)
    capacidad_mes = models.IntegerField()
    estado_mes = models.CharField(max_length=20, null=True, blank=True)



class Reservas(models.Model):
    reserva_id = models.AutoField(primary_key=True)
    fecha_reserva = models.DateField()
    hora_reserva = models.TimeField()
    numero_personas_reserva = models.IntegerField()
    estado_reserva = models.CharField(max_length=20)
    cliente = models.ForeignKey(Clientes, null=True, blank=True, on_delete=models.PROTECT)
    mesa = models.ForeignKey(Mesas, null=True, blank=True, on_delete=models.PROTECT)


    def __str__(self):
        fila="{0}: {1}"
        return fila.format(self.reserva_id,self.fecha_reserva)

#Relaciones Venta esta relacionado de 1 a muchos a detalles de ventas
class Ventas(models.Model):
    venta_id = models.AutoField(primary_key=True)
    fecha_venta = models.DateField()
    total_venta = models.IntegerField()
    cliente = models.ForeignKey(Clientes, null=True, blank=True, on_delete=models.PROTECT)

    def __str__(self):
        fila="{0}: {1}"
        return fila.format(self.venta_id,self.fecha_venta)

# Relacionado de Menu esta relacionado de 1 a Muchos a Detalles de Ventas, Promociones_menu y Detalles de Reserva

class Menus(models.Model):
    menu_id = models.AutoField(primary_key=True)
    nombre_menu = models.CharField(max_length=100)
    descripcion_menu = models.TextField()
    categoria_menu = models.CharField(max_length=100, null=True, blank=True)
    disponibilidad_menu = models.CharField(max_length=100, null=True, blank=True)
    precio_menu = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    fotos_menu=models.FileField(upload_to='menus', null=True,blank=True)

    def __str__(self):
        fila="{0}: {1}"
        return fila.format(self.menu_id,self.nombre_menu)

class Detalles_Ventas(models.Model):
    detalle_venta_id = models.AutoField(primary_key=True)
    cantidad_venta = models.IntegerField()
    precio_unitario_venta =models.DecimalField(max_digits=10, decimal_places=2)
    venta = models.ForeignKey(Ventas, null=True, blank=True, on_delete=models.PROTECT)
    menu = models.ForeignKey(Menus, null=True, blank=True, on_delete=models.PROTECT)


    def __str__(self):
        fila="{0}: {1}"
        return fila.format(self.detalle_venta_id,self.cantidad_venta)


class Detalles_Reservas(models.Model):
    detalle_reserva_id = models.AutoField(primary_key=True)
    menu = models.ForeignKey(Menus, null=True, blank=True, on_delete=models.PROTECT)
    reserva = models.ForeignKey(Reservas, null=True, blank=True, on_delete=models.PROTECT)

    def __str__(self):
        fila="{0}: {1}"
        return fila.format(self.detalle_venta_id)

#Relacion de Promociones de 1 a muchos a Promociones de menu
class Promociones(models.Model):
    promociones_id = models.AutoField(primary_key=True)
    descripcion_pro = models.TextField()
    fecha_inicio_pro = models.DateField()
    fecha_fin_pro = models.DateField()
    descuento_pro = models.DecimalField(max_digits=5, decimal_places=2)
    menu = models.ForeignKey(Menus, null=True, blank=True, on_delete=models.PROTECT)

    def __str__(self):
        fila="{0}: {1}"
        return fila.format(self.promociones_id,self.descripcion_pro)

class Recibo_Reserva(models.Model):
    cliente = models.ForeignKey(Clientes, null=True, blank=True, on_delete=models.PROTECT)
    reserva = models.ForeignKey(Reservas, null=True, blank=True, on_delete=models.PROTECT)
    total_re = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_emision_re = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        fila="{0}: {1}"
        return fila.format(self.total_re)
