from django.shortcuts import render, redirect
from django.http.response import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

def index(request):
    myapp_data = {
    'app': 'Django',
    'num': range(10),
    }
    return render(request, 'index.html', myapp_data)

def signupfunc(request):
    if request.method == 'POST':
        new_username = request.POST['username']
        new_password = request.POST['password']
        try:
            User.objects.get(username = new_username)
            return render(request, 'signup.html', {'error':'このユーザーは既に登録されています。'})
        except User.DoesNotExist:
            user = User.objects.create_user(new_username, '', new_password)
            return render(request, 'signup.html')
    else :
        print('NOT POST')
    return render(request, 'signup.html')

def loginfunc(request):
    if request.method == 'POST':
        login_username = request.POST['username']
        login_password = request.POST['password']
        user = authenticate(request, username=login_username, password=login_password)
        if user is not None:
            login(request, user)
            return redirect('signup')
        else:
            return redirect('login')
    else :
        print('NOT POST')
    return render(request, 'login.html')

def listfunc(request):
    return render(request, 'list.html')