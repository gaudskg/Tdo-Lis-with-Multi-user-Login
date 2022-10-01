from django.shortcuts import redirect, render
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from . models import Todo_task
# Create your views here.
def home(request):
    if request.user.is_authenticated:
        obj = Todo_task.objects.all().filter(user = request.user)
        context = {'task' : obj, 'msg' : 'LOGGED IN SUCCESSFULLY', 'icon' : 'success', 'title' : 'hooray....'}
        print("USER AUTHENTIC********************************")
        return render(request,'home.html',context)
    else:
        return redirect('/sign-in')
        
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
        user = authenticate(username=email, password=password)
        if user is not None:
            login(request,user)
            return redirect('/')
        else:
            context = { 'error_msg': "Please enter the correct username or password" }
            return render(request,'login.html',context)
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

def add_tasks(request):
    if request.method == 'POST':
        title = request.POST['title']
        user = Todo_task(user = request.user, title = title)
        user.save()
        return redirect('/')
    else:
        return redirect('/')

@csrf_exempt
def delete_data(request):
    if request.method == 'POST':
        task_id = request.POST['task_id']
        task = Todo_task.objects.get(id=task_id)
        task.delete()
        print(task_id)
        return JsonResponse({'task_id':task_id})
    return redirect('/')

@csrf_exempt
def change_status(request):
    if request.method == 'POST': 
        task_id = request.POST['task_id']
        user = Todo_task.objects.get(id=task_id)
        current = user.complete
        user.complete = not current
        user.save()
        print(task_id)
        return JsonResponse({'status':"ok"})
    else:
        return redirect('/')