from unicodedata import name
from django.urls import path,include
from django.http import HttpResponse
from django.shortcuts import render
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('register/', views.register, name='register'),
    path('sign-in/', views.signin, name='sign_in'),
    path('sign-up/', views.signup, name='sign_up'),
    path('sign-out/',views.signout, name='sign_out'),
    path('add-task', views.add_tasks, name='add_tasks'),
    path('delete-data', views.delete_data, name='delete_data'),
    path('change-status', views.change_status, name='change_status')
]
