from django.conf import settings
from django.db import models
from bases.models import BaseModel
from crum import get_current_user
import random



class TiposServicio(BaseModel):
    username = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField('Variedad de servicios', max_length=150)

    def __str__(self):
        return self.name

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        user = get_current_user()
        if user is not None:
            if not self.pk:
                self.user_creation = user
            else:
                self.user_updated = user
        super(TiposServicio, self).save()

    class Meta:
        verbose_name = 'Tipo de servicio'
        verbose_name_plural = 'Tipos de servicio'
        db_table = 'TipoServicio'

class Servicio(BaseModel):
    username = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    tipo_servicio = models.ForeignKey(TiposServicio, on_delete=models.CASCADE)
    no_servicio = models.AutoField(primary_key=True)
    orden_generada = models.BooleanField(default = True)
    orden_transito = models.BooleanField(default = False)

    def __str__(self):
        return '{}'.format(self.no_servicio)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        user = get_current_user()
        if user is not None:
            if not self.pk:
                self.user_creation = user
            else:
                self.user_updated = user
        super(Servicio, self).save()

    class Meta:
        verbose_name = 'Servicio'
        verbose_name_plural = 'Servicios'
        db_table = 'servicio'


class HistorialOrdenes(models.Model):
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    username = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    estado = models.ForeignKey(TiposServicio, on_delete=models.CASCADE)
    id_servicio = models.ForeignKey(Servicio, on_delete=models.CASCADE)

    def __str__(self):
        return self.id_servicio.no_servicio

    class Meta:
        verbose_name = 'Historial de servicio'
        verbose_name_plural = 'Historial de servicios'
        db_table = 'historial_servicio'


class OrdenGenerada(BaseModel):
    username = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    no_servicio = models.ForeignKey(Servicio, on_delete=models.CASCADE)
    estado = models.BooleanField(default = True, blank=True, null=True)
    nombre = models.CharField('nombre cliente', max_length=200)

    def __str__(self):
        return self.nombre

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        user = get_current_user()
        if user is not None:
            if not self.pk:
                self.user_creation = user
            else:
                self.user_updated = user
        super(OrdenGenerada, self).save()

    class Meta:
        verbose_name = 'Orden registrada'
        verbose_name_plural = 'Ordenes registradas'
        db_table = 'orden_registrada'




class Cliente(BaseModel):
    nombres = models.CharField('Nombres cliente', max_length=200)
    apellidos = models.CharField('Apellidos cliente', max_length=200)
    nit = models.CharField('NIT', max_length=20)
    tel = models.CharField('telefono', max_length=10)

    def __str__(self):
        return self.nombres

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        user = get_current_user()
        if user is not None:
            if not self.pk:
                self.user_creation = user
            else:
                self.user_updated = user
        super(Cliente, self).save()

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        db_table = 'cliente'



# class CdrByBusinessFlowID(models.Model):
#         id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#         cc_id = models.IntegerField()
#         business_flow_id = models.CharField(max_length=255, blank=True)
#         status = models.CharField(max_length=10, blank=True)
#
