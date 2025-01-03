from django.shortcuts import render

# Create your views here.


from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from forms import FormularioRegistro

# Vista de registro
def registro(request):
    if request.method == 'POST':
        formulario = FormularioRegistro(request.POST)
        if formulario.is_valid():
            usuario = formulario.save()
            login(request, usuario)  # Inicia sesión automáticamente
            return redirect('inicio')  # Cambiar inicio al nombre de tu página principal
    else:
        formulario = FormularioRegistro()
    return render(request, 'registro_usuarios/registro.html', {'formulario': formulario})

# Vista de inicio de sesión
def iniciar_sesion(request):
    if request.method == 'POST':
        formulario = AuthenticationForm(data=request.POST)
        if formulario.is_valid():
            usuario = formulario.get_user()
            login(request, usuario)
            return redirect('inicio')
    else:
        formulario = AuthenticationForm()
    return render(request, 'registro_usuarios/iniciar_sesion.html', {'formulario': formulario})

# Vista de cierre de sesión
def cerrar_sesion(request):
    logout(request)
    return redirect('iniciar_sesion')