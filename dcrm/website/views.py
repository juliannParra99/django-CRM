from django.shortcuts import render, redirect
##para manejar autenticacion con modulos de django
from django.contrib.auth import authenticate, login, logout
##maneja mensajes cuando se logea y se desloguea.
from django.contrib import messages
#i'll import the method to register
from .forms import SignUpForm

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


def register_user(request):
    # Check if the request method is POST, which means a form is being submitted
    if request.method == 'POST':
        # Create a SignUpForm instance with the data from the POST request
        form = SignUpForm(request.POST)
        
        # Check if the form's data is valid
        if form.is_valid():
            # Save the form data to create a new user
            form.save()
            
            # Authenticate and log in the newly registered user
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            
            # Show a success message to the user
            messages.success(request, "You Have Successfully Registered! Welcome!")
            
            # Redirect the user to the 'home' page
            return redirect('home')
    else:
        # If the request method is not POST, create an empty SignUpForm
        form = SignUpForm()
        
        # Render the 'register.html' template with the form
        return render(request, 'register.html', {'form': form})
    
    # Render the 'register.html' template with the form; 'form':form allow to use that form in register.html
    return render(request, 'register.html', {'form': form})