from django.shortcuts import render, redirect
##para manejar autenticacion con modulos de django
from django.contrib.auth import authenticate, login, logout
##maneja mensajes cuando se logea y se desloguea.
from django.contrib import messages

# Create your views here.
def home(request):
    # Verificar si la solicitud es un método POST (es decir, se está enviando un formulario)
    if request.method == 'POST':
        # Obtener el nombre de usuario y la contraseña desde los datos enviados en el formulario POST; username y pasword son los nombres que le asignamos los elementos en el formulario
        username = request.POST['username']
        password = request.POST['password']

        # Autenticar al usuario utilizando el nombre de usuario y contraseña proporcionados
        user = authenticate(request, username=username, password=password)

        # Verificar si la autenticación fue exitosa]: verifica si los datos ingresados corresponden con un usuario en la base de datos.Devuelve un objeto si coincide, entonces si la variable user no esta vacia hay un objeto y por lo tanto la autenticacion fue exitosa
        if user is not None:
            # Iniciar sesión al usuario autenticado
            login(request, user)
            # Agregar un mensaje de éxito a la cola de mensajes para mostrar al usuario
            messages.success(request, "You Have Been Logged In!")
            # Redirigir al usuario a la página de inicio (para mostrar la lista de registros)
            return redirect('home')
        else:
            # Si la autenticación falla, agregar un mensaje de error a la cola de mensajes
            messages.success(request, "There Was An Error Logging In, Please Try Again...")
            # Redirigir de nuevo a la página de inicio
            return redirect('home')
    else:
        # Si la solicitud no es un método POST, renderizar la plantilla 'home.html' y pasar los registros a la plantilla
        return render(request, 'home.html', {})