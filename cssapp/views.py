from django.shortcuts import render
from django.http.response import HttpResponse
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
