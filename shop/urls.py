from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('sport', views.sport, name='sport'), 
    path('view', views.view, name = 'view'),
    path("login", views.login, name="login"),
    path("logout", views.logout, name="logout"),
    path("carrito", views.carrito, name="carrito"), 
    path("pedidos", views.pedidos, name = "pedidos"), 
    path("user", views.user, name = "user"), 
    path("login_view", views.login_view, name = "login_view"), 
    path("register", views.register, name = "register"), 
    path("master", views.master, name = "master"), 
    path("logout_view", views.logout_view, name = "logout_view")
]