from django.shortcuts import render
from django.shortcuts import HttpResponse
 

# Create your views here.

def renderPrinicpal(request):
    return render(request,"/templates/menu/index.html")

def pag1(request):
    datos= {'desp':'muy buena', 'valo':'10', 'img':'/static/img/breaking.jpg'}
    return render(HttpResponse,'/templates/menu/pag2.html', datos)

def pag2(request):
    datos= {'desp':'mala', 'valo':'3', 'img':'/static/img/stranger.jpg'}
    return render(HttpResponse,'/templates/menu/pag2.html', datos)

def pag3(request):
    datos= {'desp':'buena', 'valo':'8', 'img':'/static/img/hora.jpg'}
    return render(HttpResponse,'/templates/menu/pag2.html', datos)