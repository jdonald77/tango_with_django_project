# Create your views here.

from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    context_dict = {'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!'}
    return render(request, 'rango/index.html', context=context_dict)

def about(request):
    context_dict = {'boldmessage': 'This tutorial has been put together by Joshua Donald'}
    return render(request, 'rango/about.html', context=context_dict)

def message(request):
    context_dict = {'message': 'This is my message'}
    return render(request, 'rango/message.html', context=context_dict)
