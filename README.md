# Calculadora Fatec  
Construção da Plataforma Calculadora Fatec em versão Python.

## A FAZER  
[x] Estrutura base do projeto  
[x] Rotas (Home e funcionalidades)   
[x] Instalação do boostrap v5 no base.html  
[x] Página da calculadora fatec - Home
[x] Página da ferramenta calculadora fatec
    [x] Replica do layout
    [x] Separado o conteúdo em includes
    [x] funcionalidade da lógica de cálculo via JS
[x] Página matérias de peso 2
    [x] Listagem das matérias de peso 2 por curso
    [x] Filtro de pesquisa por nome do curso
    [x] Filtro de pesquisa por eixo tecnologico
    [/] Criar o filtro de quantos itens será exibido na tabela
    [x] Mecanimo de paginação dos resultados
    [/] Lógica para filtrar itens do pesquise por nome curso sem considerar a acentuação e capslock
[x] Página escolha da Instituição      
    [x] Lógica para buscar e rederizar do ID para o Slug 
[x] Página Detalhes Instituição  
    [x] Trazer as listas de cursos ofertados na unidade    
    [x] Trazer todos os endereços sociais (facebook, ...)  
    [x] Trazer todos as formas de contato (email, telefone e whatsapp)      
    [x] Demanda dos cursos - criar relacionamento com o resultado para exibir tabela com  as demandas
        [x] Lógica de Demanda (Resultados)
        [x] Layout para exibir as demandas no template
[x] Página escolha do curso
    [x] Lógica para buscar e rederizar do ID para o Slug 
[/] Página Detalhes Curso
    [x] Adicionado os campos na model
    [-] Cadastrar informações do curso
    [x] Detalhes e informações sobre o curso
    []  Trazer relação de cursos semelhantes que o aluno possa se interessar


Para fazer import via linha de comando do sqllite
* Baixar o executável: (sqlite3.exe)[https://www.sqlite.org/download.html] (sqlite-tools-win32-x86-3400000.zip)
https://www.youtube.com/watch?v=vs6dXL9Wp7s&t=243s

> .\sqlite3.exe .\db.sqlite3
sqlite> .mode csv
sqlite> .import arquivo_de_import.csv core_nome_da_tabela
        .import resultado_fatec_1_2015.csv core_resultadovestibularfatec

https://django-import-export.readthedocs.io/en/latest/getting_started.html



https://docs.djangoproject.com/en/2.2/ref/models/querysets/#select-related

https://swapps.com/blog/quick-start-with-django-orm/
https://docs.djangoproject.com/en/4.1/topics/db/managers/


https://stackoverflow.com/questions/34904171/is-there-a-way-to-specify-the-order-of-creation-of-the-columns-for-an-sql-table
Is there a way to specify the order of creation of the columns for an SQL table conception using Django?

class My_table(models.Model):
    field1 = models.CharField(primary_key=True, max_length=25)
    field2 = models.ForeignKey(....)
    field3 = models.IntegerField(blank=True, null=True)
    field4 = models.CharField(max_length=2000, blank=True, null=True)
Can give a table like :

  field1 | field3 | field4 | field2  
 --------+--------+--------+--------
I want this :

  field1 | field2 | field3 | field4  
 --------+--------+--------+--------
Is there a way to have this result?

SOLVE:
POST MIGRATION
https://stackoverflow.com/questions/31698103/how-do-i-execute-raw-sql-in-a-django-migration
