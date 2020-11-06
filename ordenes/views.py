from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, DeleteView,TemplateView ,DetailView
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse

from ordenes.models import TiposServicio, Servicio
from ordenes.forms import TipoServicioForm, OrdenServicioForm
from django.urls import reverse_lazy


class TipoServicio(ListView):
    model =  TiposServicio
    template_name = 'ordenes/list_tipo_servicio.html'


    def get_queryset(self):
        return self.model.objects.all()

    def get_context_data(self , *args , **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context ['title'] = 'Tipos de servicio'
        context['list_url'] = reverse_lazy('ordenes:lista_servicios')
        context['new_url'] = reverse_lazy('ordenes:new_servicios')
        return context

class TipoServicioNew(CreateView):
    model = TiposServicio
    template_name = 'ordenes/create_tipo_servicio.html'
    form_class = TipoServicioForm
    success_url = reverse_lazy('ordenes:lista_servicios')

    def post(self, request, *args, **kwargs):
        form = TipoServicioForm(request.POST)
        if form.is_valid():
            self.object = form.save(commit=False)
            self.object.username = self.request.user
            form.save()
            return HttpResponseRedirect(self.success_url)
        return render(request, self.template_name, {'form': form})

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Formulario tipo de servicios'
        # context['list_perfil'] = reverse_lazy('usuario:mi_perfil')
        return context

class TipoServicioUpdate(UpdateView):
    model = TiposServicio
    template_name = 'ordenes/create_tipo_servicio.html'
    form_class = TipoServicioForm
    success_url = reverse_lazy('ordenes:lista_servicios')


    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Editar tipo de servicios'
        # context['list_perfil'] = reverse_lazy('usuario:mi_perfil')
        return context

class OrdenServicio(ListView):
    model =  Servicio
    template_name = 'ordenes/list_orden_servicio.html'


    def get_queryset(self):
        return self.model.objects.all()

    def get_context_data(self , *args , **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context ['title'] = 'Atencion al Cliente'
        context['list_url'] = reverse_lazy('ordenes:lista_ordenes_servicios')
        context['new_url'] = reverse_lazy('ordenes:new_ordenes_servicios')
        return context

class ServicioNew(CreateView):
    model = Servicio
    template_name = 'ordenes/create_orden_servicio.html'
    form_class = OrdenServicioForm
    success_url = reverse_lazy('ordenes:lista_ordenes_servicios')

    def post(self, request, *args, **kwargs):
        form = OrdenServicioForm(request.POST)
        if form.is_valid():
            self.object = form.save(commit=False)
            self.object.username = self.request.user
            form.save()
            return HttpResponseRedirect(self.success_url)
        return render(request, self.template_name, {'form': form})

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Generar No. Servicio'
        # context['list_perfil'] = reverse_lazy('usuario:mi_perfil')
        return context
