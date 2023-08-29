from django.shortcuts import render, redirect
##para manejar autenticacion con modulos de django
from django.contrib.auth import authenticate, login, logout
##maneja mensajes cuando se logea y se desloguea.
from django.contrib import messages

# Create your views here.
def home(request):
    # Verificar si la solicitud es un método POST (es decir, se está enviando un formulario)
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # Autenticar al usuario utilizando el nombre de usuario y contraseña proporcionados
        user = authenticate(request, username=username, password=password)

        
        if user is not None:
            # Iniciar sesión al usuario autenticado
            login(request, user)
            
            messages.success(request, "You Have Been Logged In!")
            
            return redirect('home')
        else:
            
            messages.success(request, "There Was An Error Logging In, Please Try Again...")
            # Redirigir de nuevo a la página de inicio
            return redirect('home')
    else:
        
        return render(request, 'home.html', {})
    
# la funcion logout de django se encarga de toda la logica.
def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out")
    return redirect('home')
      
