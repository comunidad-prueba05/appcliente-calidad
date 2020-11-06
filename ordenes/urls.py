from django.urls import path
from ordenes.views import TipoServicio, TipoServicioNew, TipoServicioUpdate, OrdenServicio, ServicioNew

urlpatterns = [
    path('lista-servicios/', TipoServicio.as_view(), name='lista_servicios'),
    path('new-servicios/', TipoServicioNew.as_view(), name='new_servicios'),
    path('update-servicios/<int:pk>/', TipoServicioUpdate.as_view(), name='update_servicios'),

    path('lista-ordenes-servicios/', OrdenServicio.as_view(), name='lista_ordenes_servicios'),
    path('new-ordenes-servicios/', ServicioNew.as_view(), name='new_ordenes_servicios'),
]
