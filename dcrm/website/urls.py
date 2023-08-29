
from django.urls import path
from . import views

# //estas son mis rutas que se van a mapear en una vista especifica.
urlpatterns = [
    path('', views.home, name="home"),
    # path('login/', views.login_user, name="login"), esta comentada, pero es en caso de querer crear un nuevo metodo que renderize otra pagina y no se realize todo el la pagina de home. En caso de querer hacerlo solo tengo que hacer lo mismo que esta en el metodo de home
    path('logout/', views.logout_user, name="logout"),
]
