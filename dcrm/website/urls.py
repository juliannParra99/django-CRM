
from django.urls import path
from . import views

# //estas son mis rutas que se van a mapear en una vista especifica.
urlpatterns = [
    path('', views.home, name="home"),
    # path('login/', views.login_user, name="login"),
    path('logout/', views.logout_user, name="logout"),
    path('register/', views.register_user, name="register"),
    #to show all data from one record in a new page; <int:pk>: This part is a URL converter. It tells Django to expect an integer value as a primary key (pk) and captures it from the URL. This captured value can then be passed as an argument to the associated view function.
    path('record/<int:pk>', views.customer_record, name="record"),
    #if we need to delete a record we want to have the ID as well. Then, we use the courve brackets
    path('delete_record/<int:pk>', views.delete_record, name="delete_record"),
]
