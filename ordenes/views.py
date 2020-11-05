from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, DeleteView,TemplateView ,DetailView

from ordenes.models import TiposServicio, Servicio
from ordenes.forms import TipoServicioForm


class TipoServicio(ListView):
    model =  TiposServicio
    template_name = 'ordenes/list_tipo_servicio.html'


    def get_queryset(self):
        return self.model.objects.all()

    def get_context_data(self , *args , **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context ['title'] = 'listado'
        return context
