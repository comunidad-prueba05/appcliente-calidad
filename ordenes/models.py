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
    no_servico = models.AutoField(primary_key=True)
    orden_generada = models.BooleanField(default = True)
    orden_transito = models.BooleanField(null=True , blank=True)

    def __str__(self):
        return self.username

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


# class CdrByBusinessFlowID(models.Model):
#         id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#         cc_id = models.IntegerField()
#         business_flow_id = models.CharField(max_length=255, blank=True)
#         status = models.CharField(max_length=10, blank=True)
#
