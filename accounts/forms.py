from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class NuestroUserForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir Contraseña', widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['username', 'email','password1', 'password2']
        helps_text = { k: '' for k in fields }

class EditFullUser(forms.Form):
    first_name = forms.CharField(label='Nombre',max_length=20)
    last_name = forms.CharField(label='Apellido',max_length=20)
    email = forms.EmailField()
    avatar = forms.ImageField(required=False)
    link = forms.URLField(required=False)
    mas_descripcion = forms.CharField(max_length=100, required=False)
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput, required=False)
    password2 = forms.CharField(label='Repetir Contraseña', widget=forms.PasswordInput, required=False)