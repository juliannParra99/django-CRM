from django.contrib import admin
#this to show our new model (table in our databese and to start to using it)
from .models import Record

# Register your models here.

#this to interact with our new model on the admin section
admin.site.register(Record)
