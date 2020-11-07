from django.urls import path
from ordenes.views import (TipoServicio, TipoServicioNew, TipoServicioUpdate, OrdenServicio, ServicioNew,
PantallList, GenerarServicio, GenerarServicioNew, ClienteList, ClienteNew, ClienteUpdate, FormularServicioList,
FormularServicioNew)

urlpatterns = [
    path('lista-servicios/', TipoServicio.as_view(), name='lista_servicios'),
    path('new-servicios/', TipoServicioNew.as_view(), name='new_servicios'),
    path('update-servicios/<int:pk>/', TipoServicioUpdate.as_view(), name='update_servicios'),

    path('lista-ordenes-servicios/', OrdenServicio.as_view(), name='lista_ordenes_servicios'),
    path('new-ordenes-servicios/', ServicioNew.as_view(), name='new_ordenes_servicios'),
    path('pantalla-servicios/', PantallList.as_view(), name='pantalla_servicios'),

    path('lista-generadas-servicios/', GenerarServicio.as_view(), name='lista_generadas_servicios'),
    path('new-generadas-servicios/', GenerarServicioNew.as_view(), name='new_generadas_servicios'),

    path('lista-cliente/', ClienteList.as_view(), name='lista_cliente'),
    path('new-cliente/', ClienteNew.as_view(), name='new_cliente'),
    path('update-cliente/<int:pk>/', ClienteUpdate.as_view(), name='update_cliente'),

    path('lista-form-servicio/', FormularServicioList.as_view(), name='lista_form_servicio'),
    path('new-form-servicio/', FormularServicioNew.as_view(), name='new_form_servicio'),

]
