from datetime import datetime
from django.forms import ModelForm, Form
from django import forms


from ordenes.models import TiposServicio, Servicio, OrdenGenerada, Cliente, FormularServicio

class TipoServicioForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['autofocus'] = True

    class Meta:
        model = TiposServicio
        fields = ['name','username']
        exclude = ['username']
        labels = {
            'name': 'Tipo de servicio',
            'username': 'Usuario'

        }
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Nombre del servicio',
                    'autocomplete': 'off'
                }
            ),
        }

class OrdenServicioForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['tipo_servicio'].widget.attrs['autofocus'] = True


    class Meta:
        model = Servicio
        fields = '__all__'
        exclude = ['username','no_servicio','orden_transito','user_creation','user_updated', 'orden_generada']
        labels = {
            'tipo_servicio': 'Elige un servicio'

        }
        widgets = {
            'tipo_servicio': forms.Select(
                attrs={
                    'class': 'form-control',
                }
            ),
        }

class OrdenGeneradaForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['no_servicio'].widget.attrs['autofocus'] = True

    class Meta:
        model = OrdenGenerada
        fields = ['no_servicio','nombre' ]
        exclude = ['username', 'estado']
        labels = {
            # 'no_servicio': 'No. Servicio',
            'nombre':'No. Ventanilla'

        }
        widgets = {
            'no_servicio': forms.Select(
                attrs={
                    'class': 'form-control select2',
                    'style': 'width: 100%'
                }
            ),
            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'autocomplete': 'off'
                }
            ),
        }
    no_servicio = forms.ModelChoiceField(queryset=Servicio.objects.filter(orden_generada=True, orden_transito=False), widget=forms.Select(attrs={
        'class': 'form-control select2',
        'style': 'width: 100%'
    }))


class ClienteForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nombres'].widget.attrs['autofocus'] = True

    class Meta:
        model = Cliente
        fields = ['nombres','apellidos','nit','tel','direccion','username']
        exclude = ['username']
        labels = {
            'nombres': 'Nombres',
            'apellidos': 'Apellidos',
            'nit': 'NIT',
            'tel': 'Telefono',
            'direccion': 'direccion'


        }
        widgets = {
            'nombres': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Nombre Completo',
                    'autocomplete': 'off'
                }
            ),
            'apellidos': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Apellidos completo',
                    'autocomplete': 'off'
                }
            ),
            'nit': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Número de Identificación Tributaria',
                    'autocomplete': 'off'
                }
            ),
            'tel': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'No. de domicilio o celular',
                    'autocomplete': 'off'
                }
            ),
            'direccion': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Dirección del domicilio',
                    'autocomplete': 'off'
                }
            ),

        }

class FormularServicioForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['no_servicio'].widget.attrs['autofocus'] = True

    class Meta:
        model = FormularServicio
        fields = ['no_servicio','cliente', 'observacion' ]
        exclude = ['username']
        labels = {
            # 'no_servicio': 'No. Servicio',
            'nombre':'No. Ventanilla'

        }
        widgets = {
            'no_servicio': forms.Select(
                attrs={
                    'class': 'form-control select2',
                    'style': 'width: 100%'
                }
            ),
            'cliente': forms.Select(
                attrs={
                    'class': 'form-control select2',
                    'style': 'width: 100%'
                }
            ),
            'observacion': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'autocomplete': 'off'
                }
            ),
        }
    no_servicio = forms.ModelChoiceField(queryset=Servicio.objects.filter(orden_generada=True, orden_transito=True), widget=forms.Select(attrs={
        'class': 'form-control select2',
        'style': 'width: 100%'
    }))
