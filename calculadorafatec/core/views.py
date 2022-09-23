from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
#Django Messages - definida lá no settings - MESSAGES_TAG
from django.contrib import messages
from django.contrib.messages import constants
# Create your views here.

def home(request):
   if request.method == "POST":
        nome = request.POST.get("nome")
        return render(request,'index.html',{'nome':nome})
   return render(request,'index.html')

def contato(request):
    return redirect('https://wa.me/5515981057742')

def logout(request):
    request.session.flush()
    return redirect(reverse('home'))    