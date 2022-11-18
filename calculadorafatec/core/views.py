from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
#Django Messages - definida lá no settings - MESSAGES_TAG
from django.contrib import messages
from django.contrib.messages import constants
from calculadorafatec.core.models import Curso, Fatec

# Create your views here.


def home(request):
    #fatecs = []
    fatecs = ['Fatec Sorocaba', 'Fatec São Roque' , 'Fatec São Paulo', 'Fatec Itu', 'Fatec Carapicuíba']

    if request.method == "POST":
            nome = request.POST.get("nome")
            return render(request,'index.html',{'nome':nome,'fatecs':fatecs})
    return render(request,'index.html',{'fatecs':fatecs})

def calculadora(request):
    return render(request,'calculadora.html')

def fatecs(request):
    #fatecs = ['Fatec Sorocaba', 'Fatec São Roque' , 'Fatec São Paulo', 'Fatec Itu', 'Fatec Carapicuíba']
    fatecs = Fatec.objects.all()
    return render(request,'fatecs.html',{'fatecs':fatecs})

def cursos(request):
    #cursos = ['Análise e Desenvolvimento de Sistemas', 'Sistemas para Internet' , 'Desenvolvimento Multiplataforma', 'Ciência de Dados', 'Sistemas Navais']
    cursos = Curso.objects.filter(ativo=True)
    return render(request,'cursos.html',{'cursos':cursos})

def materias_prova_peso2(request):
    return render(request,'materias-peso2.html')

def contato(request):
    return redirect('https://wa.me/5515981057742')

def logout(request):
    request.session.flush()
    return redirect(reverse('home'))    