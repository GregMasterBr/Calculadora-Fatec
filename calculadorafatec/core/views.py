from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
#Django Messages - definida lá no settings - MESSAGES_TAG
from django.contrib import messages
from django.contrib.messages import constants
# Create your views here.

def home(request):
    fatecs = ['Fatec Sorocaba', 'Fatec São Roque' , 'Fatec São Paulo', 'Fatec Itu', 'Fatec Carapicuíba']
    #fatecs = []
    if request.method == "POST":
            nome = request.POST.get("nome")
            return render(request,'index.html',{'nome':nome,'fatecs':fatecs})
    return render(request,'index.html',{'fatecs':fatecs})

def contato(request):
    return redirect('https://wa.me/5515981057742')

def logout(request):
    request.session.flush()
    return redirect(reverse('home'))    