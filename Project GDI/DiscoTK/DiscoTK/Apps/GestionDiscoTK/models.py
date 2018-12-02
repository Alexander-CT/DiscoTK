from django.db import models

# Create your models here.
class Cliente(models.Model): # Aqui se crean la tabla Cliente
    Nombre_cliente = models.CharField(max_length=20)
    Edad_cliente = models.PositiveSmallIntegerField()
    Direc_cliente = models.CharField(max_length=120)
    Telf_cliente =  models.CharField(max_length=9)
    def __str__(self): # Aqui se determina lo que se v a mostrar primero
        return self.Nombre_cliente

class Empleado(models.Model):
    Nombre_empleado = models.CharField(max_length=20)
    Edad_empleado = models.PositiveSmallIntegerField()
    SEXOS = (('F','Femenino'),('M','Masculino'))
    sexo_empleado = models.CharField(max_length=1, choices=SEXOS, default='M')
    CARGOS = (('B','Barman'),('S','Seguridad'),('P','Portero'),('D','DJ'))
    cargo = models.CharField(max_length=1,choices=CARGOS)
    def __str__(self):
        return self.Nombre_empleado

class Boleta(models.Model):
    Nombre_prod = models.CharField(max_length=20)
    Fecha_emision = models.DateTimeField(auto_now_add=True)
    Cliente = models.ForeignKey(Cliente, null=False,blank=False, on_delete=models.CASCADE)
    Empleado = models.ForeignKey(Empleado, null=False,blank=False, on_delete=models.CASCADE)
    def __str__(self):
        return self.Nombre_prod

class Detalle_Boleta(models.Model):
    Boleta = models.ForeignKey(Boleta, null=False, blank=False, on_delete=models.CASCADE)
    descuento = models.PositiveSmallIntegerField()
    subtotal = models.PositiveSmallIntegerField()
    IGV = models.PositiveSmallIntegerField()
    total = models.PositiveSmallIntegerField()
    def __str__(self):
        return self.descuento

class Concepto(models.Model):
    Detalle_Boleta = models.ForeignKey(Detalle_Boleta, null=False,blank=False,on_delete=models.CASCADE)
    Cant_Venta_Bebidas = models.PositiveSmallIntegerField()
    Cant_Venta_Cigarro = models.PositiveSmallIntegerField()
    Cant_Clientes_Atendidos = models.PositiveSmallIntegerField()
    def __str__(self):
        return self.Cant_Clientes_Atendidos
