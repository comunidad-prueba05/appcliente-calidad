from django.contrib.auth import authenticate
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy



from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import CreateView, ListView, UpdateView, DeleteView,TemplateView
from django.views import generic
import config.settings as setting



class SinPrivilegios(LoginRequiredMixin,PermissionRequiredMixin):
    login_url = 'bases:login'
    raise_exception=False
    redirect_field_name="redirect_to"

    def handle_no_permission(self):
        from django.contrib.auth.models import AnonymousUser
        if not self.request.user==AnonymousUser():
            self.login_url='bases:sin_privilegios'
        return HttpResponseRedirect(reverse_lazy(self.login_url))

class Login(LoginView):
    template_name = 'bases/login.html'

    def dispatch(self, request,*args, **kwargs):
        if request.user.is_authenticated:
            return redirect(setting.LOGIN_REDIRECT_URL)
        return super().dispatch(request,*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Iniciar sesión'
        return context

class Home(LoginRequiredMixin, generic.TemplateView):
    permission_required = 'base.view_usuario'
    template_name = 'bases/home.html'


class HomeSinPrivilegios(generic.TemplateView):
    template_name = 'bases/sin_privilegios.html'
