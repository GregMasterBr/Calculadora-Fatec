from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.db.models import Q
from django.http import HttpResponse,JsonResponse
from calculadorafatec.core.models import Curso, Disciplinas
from calculadorafatec.simulados.models import (
    ProcessoSeletivoVestibularFatec,
    Questao,
    Alternativa,
    SimuladoPersonalizado,
    TentativaSimulado,
    RespostaDoUsuario
)
import random


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


def simulado2(request):
    fruits = ['Apple', 'Banana', 'Cherry', 'Kiwi', 'Orange']
    disciplinas = Disciplinas.objects.all()
    return render(request,'simulado2.html',{'total_questoes':range(1,55), "fruits": fruits,'disciplinas':disciplinas})

def gabarito(request):
    return render(request,'gabarito.html',{})


@login_required
def criar_simulado_personalizado(request):
    if request.method == "POST":
        titulo = request.POST.get('titulo') or "Simulado sem título"
        questao_ids = request.POST.getlist('questoes')
        sim = SimuladoPersonalizado.objects.create(user=request.user, titulo=titulo)
        if questao_ids:
            sim.questoes.set(questao_ids)
        return redirect('simulados:ver-simulado', sim.id)
    else:
        disciplinas = Disciplinas.objects.all()
        return render(request, 'simulados/criar_simulado.html', {'disciplinas':disciplinas})

@login_required
def ver_simulado(request, simulado_id):
    sim = get_object_or_404(SimuladoPersonalizado, id=simulado_id)
    return render(request, 'simulados/ver_simulado.html', {'simulado': sim})

@login_required
def start_simulado(request, simulado_id):
    sim = get_object_or_404(SimuladoPersonalizado, id=simulado_id)
    tentativa = TentativaSimulado.objects.create(simulado=sim, user=request.user)
    return redirect('simulados:exibir-questao', tentativa.id, 1)

@login_required
def exibir_questao(request, tentativa_id, numero):
    tentativa = get_object_or_404(TentativaSimulado, id=tentativa_id, user=request.user)
    questoes = list(tentativa.simulado.questoes.all().order_by('id'))
    if numero < 1 or numero > len(questoes):
        return redirect('simulados:finalizar-tentativa', tentativa.id)
    questao = questoes[numero-1]
    alternativas = questao.alternativas.all()
    context = {
        'tentativa': tentativa,
        'questao': questao,
        'alternativas': alternativas,
        'numero': numero,
        'total': len(questoes)
    }
    return render(request, 'simulados/exibir_questao.html', context)

@login_required
def responder_questao(request, tentativa_id):
    if request.method != "POST":
        return JsonResponse({'error': 'Método inválido'}, status=400)
    tentativa = get_object_or_404(TentativaSimulado, id=tentativa_id, user=request.user)
    questao_id = int(request.POST.get('questao_id'))
    alt_id = request.POST.get('alternativa_id')
    questao = get_object_or_404(Questao, id=questao_id)
    alternativa = None
    if alt_id:
        alternativa = get_object_or_404(Alternativa, id=alt_id)
    resposta, created = RespostaDoUsuario.objects.get_or_create(
        tentativa=tentativa,
        questao=questao,
        defaults={'alternativa_marcada': alternativa}
    )
    if not created:
        resposta.alternativa_marcada = alternativa
        resposta.save()
    # next question index
    questoes = list(tentativa.simulado.questoes.all().order_by('id'))
    try:
        idx = questoes.index(questao)
        next_num = idx + 2
    except ValueError:
        next_num = None
    if next_num and next_num <= len(questoes):
        return JsonResponse({'next': reverse('simulados:exibir-questao', args=[tentativa.id, next_num])})
    else:
        return JsonResponse({'final': reverse('simulados:finalizar-tentativa', args=[tentativa.id])})

@login_required
def finalizar_tentativa(request, tentativa_id):
    tentativa = get_object_or_404(TentativaSimulado, id=tentativa_id, user=request.user)
    tentativa.finalizar()
    return render(request, 'simulados/resultado_simulado.html', {'tentativa': tentativa})


#PROVA OFICIAL DO VESTIBULAR FATEC
@login_required
def prova_oficial_detalhe(request, slug):
    processo = get_object_or_404(ProcessoSeletivoVestibularFatec, slug=slug)
    questoes = processo.questoes.prefetch_related("alternativas").all()

    return render(
        request,
        "prova-oficial/prova_oficial.html",
        {
            "processo": processo,
            "questoes": questoes,
        }
    )

@login_required
def simulado_oficial(request, slug):
    processo = get_object_or_404(ProcessoSeletivoVestibularFatec, slug=slug)
    questoes = processo.questoes.all().prefetch_related("alternativas").all()
    # Inicia a tentativa
    tentativa, created = TentativaSimulado.objects.get_or_create(
        simulado=None,   # Prova oficial não faz parte dos personalizados
        user=request.user,
        finalizado_em=None
    )

    # Criar tentativa se for POST (enviando respostas)
    if request.method == "POST":
        for q in questoes:
            alternativa_id = request.POST.get(f"questao_{q.id}")
            if alternativa_id:
                alternativa = Alternativa.objects.filter(id=alternativa_id).first()
            else:
                alternativa = None

            RespostaDoUsuario.objects.create(
                tentativa=tentativa,
                questao=q,
                alternativa_marcada=alternativa # defaults={"alternativa_marcada": alternativa}

            )

        tentativa.finalizar()

        return render(request, "prova-oficial/resultado_simulado_oficial.html", {
            "tentativa": tentativa,
            "processo": processo
        })
       # return HttpResponseRedirect(reverse("resultado-oficial", args=[slug]))


    return render(
        request,
        "prova-oficial/simulado_oficial.html",
        {"processo": processo, "questoes": questoes, "tentativa": tentativa}
    )



# Permite que o usuário escolha quantas questões quer por disciplina.
def simulado_tematico_form(request):
    disciplinas = Disciplinas.objects.all()
    return render(request, "prova-oficial/simulado_tematico_form.html", {"disciplinas": disciplinas})


def simulado_tematico_gerar(request):
    if request.method != "POST":
        return redirect("simulados:simulado-tematico-form")

    titulo = request.POST.get("titulo")
    descricao = request.POST.get("descricao")

    simulado = SimuladoPersonalizado.objects.create(
        user=request.user,
        titulo=titulo,
        descricao=descricao
    )

    # Exemplo: disciplina_1 = 5, disciplina_2 = 3
    for key, value in request.POST.items():
        if key.startswith("disciplina_") and value:
            disciplina_id = key.split("_")[1]
            quantidade = int(value)

            questoes_filtradas = list(
                Questao.objects.filter(disciplina_id=disciplina_id)
            )

            escolhidas = random.sample(questoes_filtradas, min(quantidade, len(questoes_filtradas)))
            simulado.questoes.add(*escolhidas)

    simulado.total_questoes = simulado.questoes.count()
    simulado.save()

    return redirect("simulados:simulado-tematico-resolver", simulado.id)

def simulado_tematico_resolver(request, simulado_id):
    simulado = get_object_or_404(SimuladoPersonalizado, id=simulado_id)
    questoes = simulado.questoes.all()

    if request.method == "POST":
        tentativa = TentativaSimulado.objects.create(
            simulado=simulado,
            user=request.user
        )

        for q in questoes:
            alternativa_id = request.POST.get(f"questao_{q.id}")
            alternativa = Alternativa.objects.filter(id=alternativa_id).first() if alternativa_id else None

            RespostaDoUsuario.objects.create(
                tentativa=tentativa,
                questao=q,
                alternativa_marcada=alternativa
            )

        tentativa.finalizar()

        return render(request, "prova-oficial/resultado_simulado_tematico.html", {
            "tentativa": tentativa,
            "simulado": simulado
        })

    return render(
        request,
        "prova-oficial/simulado_tematico_resolver.html",
        {"simulado": simulado, "questoes": questoes}
    )
