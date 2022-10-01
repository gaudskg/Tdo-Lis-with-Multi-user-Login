from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

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
            return render(request,'login.html',context)
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
        username = request.POST['username']
        name = request.POST['user_name']
        email = request.POST['user_email']
        password = request.POST['user_password']
        confirm_password = request.POST['user_confirm_password']
        print(username,name,email,password,confirm_password,"******************************")
        if password == confirm_password:
            user = User.objects.create_user(username, email, password)
            user.first_name = name
            user.save()
            context = {
                'success_msg' : f"Hi {name}, your account has been generated successfully"
            }
            return render(request,'login.html',context)
        elif password != confirm_password:
            context = {'error_msg' : 'Registration Failed, Please Enter the correct Info'}
            return render(request,'register.html',context)
        
    # return render(request,'login.html')
    return render(request,'register.html')

def signout(request):
    logout(request)
    return redirect('/sign-in')