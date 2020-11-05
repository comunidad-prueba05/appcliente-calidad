from datetime import datetime
from django.forms import ModelForm, Form
from django import forms


from ordenes.models import TiposServicio, Servicio

class TipoServicioForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['autofocus'] = True

    class Meta:
        model = TiposServicio
        fields = ['name','username']
        labels = {
            'name': 'Tipo de servicio',
            'username': 'Usuario'

        }
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese una Dirección',
                    'autocomplete': 'off'
                }
            ),
            'username': forms.TextInput(
                attrs={
                    'class': 'form-control',
                }
            ),
        }
