# Import necessary modules from Django
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


# El método __init__ personalizado dentro de la clase SignUpForm se encarga de modificar la apariencia y el comportamiento de los campos específicos en el formulario de registro. Se enfoca en los campos 'username', 'password1' y 'password2' y ajusta las clases de estilo CSS, los marcadores de posición, las etiquetas y los mensajes de ayuda para mejorar la experiencia del usuario durante el proceso de registro. Los campos restantes definidos en la propiedad fields de la clase Meta ('first_name', 'last_name' y 'email') heredan comportamientos de personalización predefinidos del formulario base UserCreationForm. Si se desea, las personalizaciones similares pueden aplicarse a esos campos mediante la extensión de este método o la configuración en la clase Meta.


# This class definition SignUpForm is a custom form that inherits from Django's built-in UserCreationForm. The purpose of this form is to collect user registration information. Here, three additional fields are being added:
# Define a custom form named SignUpForm that inherits from UserCreationForm
class SignUpForm(UserCreationForm):
    # Define additional fields for the form
    email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email Address'}))
    first_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'First Name'}))
    last_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last Name'}))

    # Define the form's meta information
    class Meta:
        model = User  # Use the User model
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')  # Specify the fields to include in the form

    # Customize the form's initialization process
    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        # Customize attributes of the 'username' field
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'User Name'
        self.fields['username'].label = ''
        self.fields['username'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'

        # Customize attributes of the 'password1' field
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].label = ''
        self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'

        # Customize attributes of the 'password2' field
        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['password2'].label = ''
        self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'