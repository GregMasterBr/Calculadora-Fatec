from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
#Django Messages - definida lá no settings - MESSAGES_TAG
from django.contrib import messages
from django.contrib.messages import constants
from calculadorafatec.core.models import Curso, Fatec, ResultadoVestibularFatec, EixoTecnologico, Social, Contact
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
    #resultados_cursos = ResultadoVestibularFatec.objects.filter(cod_instituicao=fatec.id)
    #resultados_cursos = ResultadoVestibularFatec.objects.all().order_by('-ano', '-semestre')
    #resultados_cursos.intersection(cursos).values()
    resultados_cursos = ResultadoVestibularFatec.objects.filter(cod_instituicao=fatec.id).order_by('-ano', '-semestre')
    #resultados_cursos2 = ResultadoVestibularFatec.objects.select_related('cursos').filter(cod_instituicao=fatec.id)
    #resultados_cursos2 = ResultadoVestibularFatec.objects.filter(cod_instituicao=fatec.id).join(cod_curso=cursos.id,from={"cursos":"cursos"})
    #resultados_cursos2 = ResultadoVestibularFatec.objects.filter(cod_instituicao=fatec.id).extra(select={'curso':'SELECT curso FROM "Curso" WHERE "ResultadoVestibularFatec".cod_curso = "Curso".id'})
    # raw_sql = """SELECT * FROM 

	# (SELECT * FROM "ResultadoVestibularFatec" WHERE cod_instituicao = my_id) as "RVF" INNER JOIN  
	# "Curso" as "C" ON "C".id = "RVF".cod_curso ;"""
    raw_sql = """
            SELECT RVF.*, C.curso as nomecurso FROM ResultadoVestibularFatec as RVF
            INNER JOIN  
            Curso as C
            ON "RVF".cod_curso = C.id;
            
            """    

    #resultados_cursos2 = ResultadoVestibularFatec.objects.raw(raw_sql)
    #kwds= ResultadoVestibularFatec.objects.filter(cod_instituicao=fatec.id).join(ResultadoVestibularFatec_id__in = Curso.id)

    #print(resultados_cursos.union(cursos))

    #print(resultados_cursos2)
    resultados_cursos2 = []


    #print(resultados_cursos.values())
    return render(request,'detalhes-fatec.html', {'detalhe': fatec,'cursos':cursos, 'redessociais': socialmedia, 'contatos': contatos, 'resultados':resultados_cursos, 'resultado2' :resultados_cursos2 })   


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