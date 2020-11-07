from django.shortcuts import render

from django.views.generic import CreateView, ListView, UpdateView, DeleteView,TemplateView
from django.urls import reverse_lazy
from usuario.models import User
from usuario.forms import FormularioUser


class UserList(ListView):
    model = User
    template_name = 'usuario/list_usuario.html'

    def get_queryset(self):
        return self.model.objects.all()

    def get_context_data(self , *args , **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context ['title'] = 'Usuario Administrativos'
        context['list_url'] = reverse_lazy('usuario:list_usuario')
        context['new_url'] = reverse_lazy('usuario:new_usuario')
        return context

class RegistrarUser(CreateView):
    model = User
    form_class = FormularioUser
    template_name = 'usuario/crear_usuario.html'
    success_url = reverse_lazy('usuario:list_usuario')

    def get_context_data(self , *args , **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context ['title'] = 'Registrar Usuario'
        return context

class UserUpdate(UpdateView):
    model = User
    form_class = FormularioUser
    template_name = 'usuario/crear_usuario.html'
    success_url = reverse_lazy('user:user_listlist_usuario')

    def get_context_data(self , *args , **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context ['title'] = 'Editar Usuario'
        return context
