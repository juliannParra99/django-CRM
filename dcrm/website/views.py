from django.shortcuts import render, redirect
##para manejar autenticacion con modulos de django
from django.contrib.auth import authenticate, login, logout

from django.contrib import messages
from .forms import SignUpForm, AddRecordForm
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
   

def add_record(request):
    return render(request, 'add_record.html', {})


#Add record
def add_record(request):
    # Create an instance of the 'AddRecordForm' form class, 
    form = AddRecordForm(request.POST or None)
    
    # Check if the user is authenticated (logged in)
    if request.user.is_authenticated:
        # Check if the request method is POST (usually from a form submission)
        if request.method == "POST":
            # Check if the form data is valid
            if form.is_valid():
                # Save the form data as a new record in the database
                add_record = form.save()
                # Display a success message to the user
                messages.success(request, "Record Added...")
                # Redirect the user to the 'home' page
                return redirect('home')
        # Render the 'add_record.html' template with the form if it's not a POST request or if the form is invalid
        return render(request, 'add_record.html', {'form': form})
    else:
        # If the user is not authenticated, display a message and redirect to the 'home' page
        messages.success(request, "You Must Be Logged In...")
        return redirect('home')

def update_record(request, pk):
    # Check if the user is authenticated (logged in)
    if request.user.is_authenticated:
        # Get the current record to be updated based on the provided 'pk' (primary key)
        current_record = Record.objects.get(id=pk)
        
        # Create an instance of the 'AddRecordForm' form class, initialized with the current record's data

        # It creates an instance of the AddRecordForm form class and initializes it with the data from the current record. This allows the form to be pre-filled with the existing record's data for editing.
        form = AddRecordForm(request.POST or None, instance=current_record)
        
        # Check if the form data is valid
        if form.is_valid():
            # Save the form data to update the existing record in the database
            form.save()
            # Display a success message to the user
            messages.success(request, "Record Has Been Updated!")
            # Redirect the user to the 'home' page
            return redirect('home')
        
        # Render the 'update_record.html' template with the form if it's not valid or not a POST request
        return render(request, 'update_record.html', {'form': form})
    else:
        # If the user is not authenticated, display a message and redirect to the 'home' page
        messages.success(request, "You Must Be Logged In...")
        return redirect('home')