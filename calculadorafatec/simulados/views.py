from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from calculadorafatec.core.models import Curso
from calculadorafatec.simulados.models import ProcessoSeletivoVestibularFatec
# Create your views here.


def home_simulados(request):
    cursos = Curso.objects.filter(ativo=True)
    processos_seletivos = ProcessoSeletivoVestibularFatec.objects.all().order_by('-simulado_gratuito','-ano', '-semestre')

    return render(request,'index-simulados.html',{'cursos':cursos, 'processos_seletivos': processos_seletivos})

def teste_simulado(request):
    curso_id = request.POST.get('cod_curso')
    prova_vestibular_edicao_slug = request.POST.get('prova_vestibular')
    prova_vestibular_edicao = get_object_or_404(ProcessoSeletivoVestibularFatec, slug=prova_vestibular_edicao_slug) 
    #curso1 = Curso.objects.filter(id=curso_id).first()
    #curso2 = Curso.objects.get(id=curso_id)
    curso = get_object_or_404(Curso, id=curso_id)  

    
    return render(request,'simulado.html',{'curso':curso, 'prova_vestibular_edicao': prova_vestibular_edicao})

