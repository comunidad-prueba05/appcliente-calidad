from django.urls import path
from ordenes.views import TipoServicio

urlpatterns = [
    path('lista-servicios', TipoServicio.as_view(), name='lista_servicios'),
]
