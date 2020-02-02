from django.urls import path

from .views import index, signupfunc, loginfunc, listfunc

urlpatterns = [
    path('', index, name='index'),
    path('signup/', signupfunc, name='signup'),
    path('login/',loginfunc, name='login'),
    path('list/',listfunc, name='list'),
]