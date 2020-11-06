from django.contrib import admin
from ordenes.models import TiposServicio, Servicio, OrdenGenerada

admin.site.register(TiposServicio)
admin.site.register(Servicio)
admin.site.register(OrdenGenerada)
