from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
#Django Messages - definida lá no settings - MESSAGES_TAG
from django.contrib import messages
from django.contrib.messages import constants
# Create your views here.

def home(request):
    return render(request,'index.html')    
    return HttpResponse('Seja bem-vindo a HOME')


def logout(request):
    request.session.flush()
    return redirect(reverse('login'))    