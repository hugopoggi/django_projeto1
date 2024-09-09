from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request,'recipes/home.html', context={
        'name': 'Hugo Poggi'
    })

def contact(resquest):
    return HttpResponse('Contato')

def about(request):
    return HttpResponse('Sobre')

