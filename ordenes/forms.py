from datetime import datetime
from django.forms import ModelForm, Form
from django import forms


from ordenes.models import TiposServicio, Servicio, OrdenGenerada

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
                    'class': 'form-control'
                }
            ),
        }
    no_servicio = forms.ModelChoiceField(queryset=Servicio.objects.filter(orden_generada=True, orden_transito=False), widget=forms.Select(attrs={
        'class': 'form-control select2',
        'style': 'width: 100%'
    }))
