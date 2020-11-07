from django import forms
from django.contrib.auth.forms import AuthenticationForm
from usuario.models import User


class FormularioUser(forms.ModelForm):
    # """ Formulario de Registro de un Usuario en la base de datos
    #
    # Variables:
    #
    #     - password1:    Contraseña
    #     - password2:    Verificación de la contraseña
    #
    # """

    password2 = forms.CharField(label = 'Contraseña de Confirmación', min_length=7, widget = forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Ingrese nuevamente su contraseña...',
            'id': 'password2',
            'required': 'required',
            'min_length': 7,
            'autocomplete': 'off'
        }
    ))


    class Meta:
        model = User
        fields = 'first_name', 'last_name', 'email', 'username', 'password', 'groups'
        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese sus nombres',
                    'autocomplete': 'off',
                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese sus apellidos',
                    'autocomplete': 'off',
                }
            ),
            'email': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese su email',
                    'autocomplete': 'off',
                }
            ),
            'username': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese su username',
                    'autocomplete': 'off',
                }
            ),
            'password': forms.PasswordInput(render_value=True,
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese su password',
                    'autocomplete': 'off',
                }
            ),

        }
        exclude = ['user_permissions', 'last_login', 'date_joined', 'is_superuser', 'is_active', 'is_staff', 'groups']

    def clean_password2(self):
        # """ Validación de Contraseña
        #
        # Metodo que valida que ambas contraseñas ingresadas sean igual, esto antes de ser encriptadas
        # y guardadas en la base dedatos, Retornar la contraseña Válida.
        #
        # Excepciones:
        # - ValidationError -- cuando las contraseñas no son iguales muestra un mensaje de error
        # """
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        if password != password2:
            raise forms.ValidationError('Contraseñas no coinciden!')
        return password2

    def save(self,commit = True):
        user = super().save(commit = False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user

    def clean_username(self):
        username = self.cleaned_data.get('username')

        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('El username ya se encuenta en uso')
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')

        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('El email ya se encuenta en uso')
        return email




# class UpdateUsuario(forms.ModelForm):
#
#
#     class Meta:
#         model = Usuario
#         fields = ('email','username','nombres','apellidos','nit', 'telefono')
#         widgets = {
#             'email': forms.EmailInput(
#                 attrs = {
#                     'class': 'form-control',
#                     'placeholder': 'Correo Electrónico',
#                     'autocomplete': 'off',
#                     'readonly': True,
#                 }
#             ),
#             'nombres': forms.TextInput(
#                 attrs={
#                     'class': 'form-control',
#                     'placeholder': 'Ingrese sus nombre',
#                     'autocomplete': 'off',
#                 }
#             ),
#             'apellidos': forms.TextInput(
#                 attrs = {
#                     'class': 'form-control',
#                     'placeholder': 'Ingrese sus apellidos',
#                     'autocomplete': 'off',
#                 }
#             ),
#             'username': forms.TextInput(
#                 attrs = {
#                     'class': 'form-control',
#                     'placeholder': 'Ingrese su nombre de usuario',
#                     'autocomplete': 'off',
#                     'readonly': True,
#                 }
#             ),
#             'telefono': forms.TextInput(
#                 attrs = {
#                     'class': 'form-control',
#                     'placeholder': 'No. Telefonico',
#                     'autocomplete': 'off'
#                 }
#             ),
#             'nit': forms.TextInput(
#                 attrs = {
#                     'class': 'form-control',
#                     'placeholder': '',
#                     'autocomplete': 'off'
#                 }
#             ),
#
#
#         }
