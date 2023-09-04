# Importing necessary modules from Django
from django.db import models


##with all this djanjo make a table in our database just using  python code. To complete the process we need to execute the commands : makemigrations and migrations
# Defining a Django model called 'Record'
class Record(models.Model):
    # 'created_at' field automatically records the creation timestamp
    created_at = models.DateTimeField(auto_now_add=True)

    # 'first_name' field to store the first name, limited to 50 characters
    first_name = models.CharField(max_length=50)

    # 'last_name' field to store the last name, limited to 50 characters
    last_name = models.CharField(max_length=50)

    # 'email' field to store the email address, limited to 100 characters
    email = models.CharField(max_length=100)

    # 'phone' field to store the phone number, limited to 15 characters
    phone = models.CharField(max_length=15)

    # 'address' field to store the address, limited to 100 characters
    address = models.CharField(max_length=100)

    # 'city' field to store the city, limited to 50 characters
    city = models.CharField(max_length=50)

    # 'state' field to store the state, limited to 50 characters
    state = models.CharField(max_length=50)

    # 'zipcode' field to store the ZIP code, limited to 20 characters
    zipcode = models.CharField(max_length=20)

    # '__str__' method defines a human-readable representation of the model
    def __str__(self):
        # It returns a string in the format "First Name Last Name"
        return f"{self.first_name} {self.last_name}"
