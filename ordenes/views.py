from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, DeleteView,TemplateView ,DetailView
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse

from ordenes.models import TiposServicio, Servicio, OrdenGenerada
from ordenes.forms import TipoServicioForm, OrdenServicioForm, OrdenGeneradaForm
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

class PantallList(TemplateView):
    template_name = 'ordenes/list_pantalla.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Atención al cliente'
        context['subtitle'] = 'Número de atención'
        context['list_url'] = reverse_lazy('ordenes:pantalla_servicios')
        context['list_home'] = reverse_lazy('bases:home')
        context['generar_orden'] = Servicio.objects.filter(orden_generada=True, orden_transito=False)
        context['transito_orden'] = Servicio.objects.filter(orden_transito=True, orden_generada=True )
        return context

class GenerarServicio(ListView):
    model =  OrdenGenerada
    template_name = 'ordenes/list_tipo_servicio_generada.html'


    def get_queryset(self):
        return self.model.objects.all()

    def get_context_data(self , *args , **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context ['title'] = 'Generar Orden de Servicio'
        context['list_url'] = reverse_lazy('ordenes:lista_generadas_servicios')
        context['new_url'] = reverse_lazy('ordenes:new_generadas_servicios')
        return context

class GenerarServicioNew(CreateView):
    model = OrdenGenerada
    template_name = 'ordenes/create_orden_generada_servicio.html'
    form_class = OrdenGeneradaForm
    success_url = reverse_lazy('ordenes:lista_generadas_servicios')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Formulario de atención'
        # context['list_perfil'] = reverse_lazy('usuario:mi_perfil')
        return context


    def post(self, request, *args, **kwargs):
        form = OrdenGeneradaForm(request.POST)
        if form.is_valid():
            self.object = form.save(commit=False)
            self.object.username = self.request.user
            id_servicio = self.object.no_servicio.pk
            servicio_update = Servicio.objects.get(pk=id_servicio)
            servicio_update.orden_transito = True
            form.save()
            servicio_update.save()
            return HttpResponseRedirect(self.success_url)
        return render(request, self.template_name, {'form': form})



# class DatosServicioNew(CreateView):
#     model = OrdenGenerada
#     template_name = 'ordenes/create_orden_generada_servicio.html'
#     form_class = OrdenGeneradaForm
#     success_url = reverse_lazy('ordenes:lista_generadas_servicios')
#
#     def get_context_data(self, *args, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['title'] = 'Formulario de atención'
#         # context['list_perfil'] = reverse_lazy('usuario:mi_perfil')
#         return context
#
#
#     def post(self, request, *args, **kwargs):
#         form = OrdenGeneradaForm(request.POST)
#         if form.is_valid():
#             self.object = form.save(commit=False)
#             self.object.username = self.request.user
#             id_servicio = self.object.no_servicio.pk
#             servicio_update = Servicio.objects.get(pk=id_servicio)
#             servicio_update.orden_transito = False
#             servicio_update.orden_transito = False
#             form.save()
#             servicio_update.save()
#             return HttpResponseRedirect(self.success_url)
#         return render(request, self.template_name, {'form': form})
