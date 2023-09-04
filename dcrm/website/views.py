from django.shortcuts import render, redirect
##para manejar autenticacion con modulos de django
from django.contrib.auth import authenticate, login, logout

from django.contrib import messages
from .forms import SignUpForm
#I grab the model with my data to show it on the page
from .models import Record

# Create your views here.
def home(request):

    #asign to this variable ALL the records   inside the model records
    records =Record.objects.all()


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
        #if the user is logged we want to show the rocors on home
        return render(request, 'home.html', {'records':records})
    
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


#method to show a particular record; recive a pk difinede on the urls.py : <int:pk>; to return the record with that pk
def customer_record(request, pk):
    # Check if the user is authenticated (logged in).
    if request.user.is_authenticated:
        # If the user is logged in, proceed with the following steps:

        # Look up a record from the 'Record' model using the provided primary key 'pk'.
        #just one record, by k
        customer_record = Record.objects.get(id=pk)

        # Render the 'record.html' template with the 'customer_record' as context data.
        #we will provide the record in the variable customer_record to pass it to the page
        return render(request, 'record.html', {'customer_record': customer_record})

    else:
        # If the user is not authenticated (not logged in), do the following:

        # Display a success message using Django's messaging framework.
        messages.success(request, "You Must Be Logged In To View That Page...")

        # Redirect the user to the 'home' URL (assumes there is a 'home' URL pattern defined in your Django app).
        return redirect('home')


def delete_record(request, pk):
    if request.user.is_authenticated:
        delete_it = Record.objects.get(id=pk)
        delete_it.delete()
        messages.success(request, "Record Deleted Successfully.")
        return redirect('home')
    else:
        messages.success(request, "You Must Be Logged In.")
        return redirect('home')
   