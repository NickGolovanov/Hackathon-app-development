from  django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name = 'index-page'),
    path('login',views.login,name = 'login-page'),


]