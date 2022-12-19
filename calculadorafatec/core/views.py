from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
#Django Messages - definida lá no settings - MESSAGES_TAG
from django.contrib import messages
from django.contrib.messages import constants
from calculadorafatec.core.models import Curso, Fatec, ResultadoVestibularFatec, ResultadoVestibularFatec2, EixoTecnologico, Social, Contact
from django.conf import settings
from django.core.paginator import (
    Paginator,
    EmptyPage,
    PageNotAnInteger,
)


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


def busca_slug_fatec(request):
    id = request.GET.get('cod_fatec')
    if id != "0":
        fatec = get_object_or_404(Fatec, id=id) #capturar a excessão aqui
        return redirect('detalhes_fatec', fatec.slug)    
    return redirect('fatecs')    


def detalhes_fatec(request, slug):
    fatec = get_object_or_404(Fatec, slug=slug)   
    fatec.imagem = f'{settings.MEDIA_URL}{fatec.imagem}'
    todos_cursos = Curso.objects.all()
    cursos = Curso.objects.filter(fatec__id=fatec.id)
    socialmedia =  Social.objects.filter(Fatec_id=fatec.id)
    contatos =  Contact.objects.filter(Fatec_id=fatec.id)
    resultados_cursos = ResultadoVestibularFatec.objects.filter(cod_instituicao=fatec.id).order_by('-ano', '-semestre')
    #resultados_cursos2 = ResultadoVestibularFatec2.objects.filter(cod_instituicao=fatec.id).order_by('-ano', '-semestre').values_list('cod_curso', 'periodo')
    resultados_cursos2 = ResultadoVestibularFatec2.objects.filter(cod_instituicao=fatec.id).order_by('cod_curso_id','periodo','-ano', '-semestre')

    demanda = {}

    for resultado in resultados_cursos2:        
        r = {}
        curso_periodo_key = ' - '.join([str(resultado.cod_curso),resultado.periodo])
        
        if curso_periodo_key not in demanda:
            demanda[curso_periodo_key] = []            
              
        if curso_periodo_key in demanda:
            r = {
                "curso": str(resultado.cod_curso),
                "id_curso": resultado.cod_curso_id,
                "periodo": resultado.periodo,
                "ano": resultado.ano,
                "semestre":resultado.semestre,
                "qtde_vagas": resultado.qtde_vagas,
                "qtde_inscrito": resultado.qtde_inscrito,
                "demanda": resultado.demanda,
                "nota_corte":resultado.nota_corte,
                "nota_maxima":resultado.nota_maxima                
            }
           # aux = demanda[curso_periodo_key]
                   
    
            demanda[curso_periodo_key].append(r)
    print(demanda)
    for key, value in demanda.items():
        print((value))
    return render(request,'detalhes-fatec.html', {
        'detalhe': fatec,'cursos':cursos, 
        'redessociais': socialmedia, 'contatos': contatos, 
        'resultados':resultados_cursos, 'resultado2' :resultados_cursos2, "demandasCursos":  demanda
        })   

def busca_slug_curso(request):
    id = request.GET.get('cod_curso')
    if id != "0":
        curso = get_object_or_404(Curso, id=id) #capturar a excessão aqui
        return redirect('detalhes_curso', curso.slug)    
    return redirect('cursos')    

def detalhes_curso(request, slug):
    curso = get_object_or_404(Curso, slug=slug) 
    fatecs = Fatec.objects.filter(cursos=curso.id)
    return render(request,'detalhes-curso.html', {'detalhe': curso,'fatecs':fatecs })   

def cursos(request):
    #cursos = ['Análise e Desenvolvimento de Sistemas', 'Sistemas para Internet' , 'Desenvolvimento Multiplataforma', 'Ciência de Dados', 'Sistemas Navais']
    cursos = Curso.objects.filter(ativo=True)
    return render(request,'cursos.html',{'cursos':cursos})

def materias_prova_peso2_com_js(request):
    return render(request,'materias-peso2-com-js.html')


def materias_prova_peso2(request):
    default_page = 1
    quantidade_ = request.GET.get('quantidades_cursos')
  
    if quantidade_:
        default_page = quantidade_

    page = request.GET.get('page', default_page)

    eixo_filtrar = request.GET.get('eixo-texnologico')
    nome_curso_filtrar = request.GET.get('nome-curso')

    cursos = Curso.objects.all()

    if eixo_filtrar:
        cursos = cursos.filter(eixo_tecnologico = eixo_filtrar)
    else:
        eixo_filtrar = 0
    
    if nome_curso_filtrar:
        cursos = cursos.filter(curso__icontains = nome_curso_filtrar)   
    else:
        nome_curso_filtrar = ""

    eixo_tecnologicos = EixoTecnologico.objects.all()    

    # Paginate items
    items_per_page = 2
    paginator = Paginator(cursos, items_per_page)  

    try:
        items_cursos_page = paginator.page(page)
    except PageNotAnInteger:
        items_cursos_page = paginator.page(default_page)
    except EmptyPage:
        items_cursos_page = paginator.page(paginator.num_pages)          

    # Provide filtered, paginated library items
    return render(request,'materias-peso2.html',{'cursos':cursos, 'eixo_tecnologicos':eixo_tecnologicos,'items_cursos_page':items_cursos_page, 'pesquisa_nome_curso':nome_curso_filtrar, 'pesquisa_eixo_tecnologico': int(eixo_filtrar) })


def contato(request):
    return redirect('https://wa.me/5515981057742')


def logout(request):
    request.session.flush()
    return redirect(reverse('home'))    