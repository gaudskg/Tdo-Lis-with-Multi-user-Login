from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
# Create your views here.

def home(request):
    if request.method == 'POST':
        email = request.POST['user_email']
        password = request.POST['user_password']
        print(email,password,"***********************************")
        user = authenticate(username=email, password=password)
        if user is not None:
            login(request,user)
            return redirect('/')
        else:
            context = { 'error_msg': "Please enter the correct username or password" }
            return redirect('/sign-in',context)
    return render(request,'home.html')

def register(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        return render(request,'register.html')

def signin(request):
    if request.method == 'POST':
        email = request.POST['user_email']
        password = request.POST['user_password']
        print(email,password,"***********************************")
        user = authenticate(email=email, password=password)
        if user is not None:
            login(request,user)
            return redirect('/')
        else:
            context = { 'error_msg': "Please enter the correct username or password" }
            return redirect('/sign-in',context)
    return render(request,'login.html')

def signup(request):
    if request.method == 'POST':
        name = request.POST['user_name']
        email = request.POST['user_email']
        password = request.POST['user_password']
        confirm_password = request.POST['user_confirm_password']
        print(name,email,password,confirm_password,"******************************")
    # return render(request,'login.html')
    return HttpResponse("SIGNUP PAGE")

def signout(request):
    logout(request)
    return redirect('/sign-in')