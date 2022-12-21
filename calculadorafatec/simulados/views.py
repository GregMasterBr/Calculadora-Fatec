from django.shortcuts import render
from calculadorafatec.core.models import Curso
# Create your views here.


def home_simulados(request):
    cursos = Curso.objects.filter(ativo=True)
    return render(request,'index-simulados.html',{'cursos':cursos})