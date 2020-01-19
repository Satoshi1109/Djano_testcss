from django.shortcuts import render
from django.http.response import HttpResponse

def index(request):
    myapp_data = {
    'app': 'Django',
    'num': range(10),
    }
    return render(request, 'index.html', myapp_data)
