from django.shortcuts import render
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
    atrris = request.POST.get('cod_curso')
    curso = request.POST['cod_curso']

    print(curso)
    
    return HttpResponse(f'Teste Simulado { curso_id } { curso }' )