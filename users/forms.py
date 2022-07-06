from django import forms
from .models import User
from django.contrib.auth import authenticate

class UserRegisterForm(forms.ModelForm):

    password1 = forms.CharField(
        label='Contraseña',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder':'Repetir Contraseña'
            }
        )
    )
    password2 = forms.CharField(
        label='Contraseña',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder':'Repetir Contraseña'
            }
        )
    )

    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'nombres',
            'apellidos',
            'genero',
            'image_user',
            'link',
        )

    def clean_password2(self):
        if self.cleaned_data['password1'] != self.cleaned_data['password2']:
            self.add_error('password2', 'Las contraseñas no son iguales')

class LoginForm(forms.Form):

    username = forms.CharField(
        label='username',
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder':'Username',
                'style': '{ margin: 10px }'
            }
        )
    )
    password = forms.CharField(
        label='Contraseña',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder':'Contraseña'
            }
        )
    )

    def clean(self):
        cleaned_data = super(LoginForm, self).clean()
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']

        if not authenticate(username=username, password=password):
            raise forms.ValidationError('Los datos de usuario no son correctos')

        return self.cleaned_data


class UpdatePasswordForm(forms.Form):

    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'nombres',
            'apellidos',
            'genero',
            'image_user',
            'link',
            'geeks_field'
        )
    email= forms.EmailField(label="Nuevo email", required=False)   
    nombres= forms.CharField(label="Nuevo nombre", required=False)
    apellidos= forms.CharField(label="Nuevo apellido", required=False)
    geeks_field = forms.FileField(label="Nueva imagen", required=False)
    link= forms.CharField(label="Nuedo link", required=False)

    password1 = forms.CharField(
        label='Contraseña',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder':'Contraseña Actual'
            }
        )
    )
    password2 = forms.CharField(
        label='Contraseña',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder':'Contraseña Nueva'
            }
        )
    )
    email= forms.EmailField(label="Nuevo email", required=False)   
    nombres= forms.CharField(label="Nuevo nombre", required=False)
    apellidos= forms.CharField(label="Nuevo apellido", required=False)
    geeks_field = forms.FileField(label="Nueva imagen", required=False)
    link= forms.CharField(label="Nuedo link", required=False)

