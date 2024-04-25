from django.urls import path
from . import views

urlpatterns = [
    path('', views.signin, name='signin'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('admin', views.admin, name='admin'),
]