
from django.urls import path
from . import views

# //estas son mis rutas que se van a mapear en una vista especifica.
urlpatterns = [
    path('', views.home, name="home"),
    # path('login/', views.login_user, name="login"),
    path('logout/', views.logout_user, name="logout"),
    path('register/', views.register_user, name="register"),
]
