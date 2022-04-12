from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from .forms import NuestroUserForm

def mi_login(request):
    
    msj = ''
    
    if request.method == 'POST':
        login_form = AuthenticationForm(request, data = request.POST)
        
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            
            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                msj = 'El usuario no se pudo autenticar'
        else:
            msj = 'El formulario no es valido'
     
    login_form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'login_form': login_form, 'msj': msj})

def registrarse(request):
    if request.method == 'POST':
        form = NuestroUserForm(request.POST)
        
        if form.is_valid():
            username = form.cleaned_data['username']
            form.save()
            return render(request, 'accounts/index.html', {'msj': f' Se creo correctamente al usuario {username}'})
        else:
            return render(request, 'accounts/registrarse.html', {'form': form, 'msj':'El formulario no es valido'})
        
    form = NuestroUserForm()
    return render(request, 'accounts/registrarse.html', {'form': form})