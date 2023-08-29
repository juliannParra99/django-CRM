
from django.urls import path
from . import views

# //estas son mis rutas que se van a mapear en una vista especifica.
urlpatterns = [
    path('', views.home, name="home"),
    # path('login/', views.home, name="login"),
    # path('logout/', views.home, name="logout"),
]
