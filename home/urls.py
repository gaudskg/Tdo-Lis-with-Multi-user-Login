from django.urls import path,include
from django.http import HttpResponse
from django.shortcuts import render
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('register/', views.register, name='register'),
    path('sign-in/', views.signin, name='sign_in'),
    path('sign-up/', views.signup, name='sign_up'),
    path('sign-out/',views.signout, name='sign_out')
]
