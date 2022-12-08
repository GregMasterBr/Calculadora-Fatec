# Calculadora Fatec  
Construção da Plataforma Calculadora Fatec em versão Python.

## A FAZER  
[x] Estrutura base do projeto  
[x] Rotas (Home e funcionalidades)   
[x] Instalação do boostrap v5 no base.html  
[x] Página da calculadora fatec
[x] Página matérias de peso 2
    [/] Criar o filtro de quantos itens será exibido na tabela
[x] Página escolha da Instituição  
[/] Página Detalhes Instituição  
    [x] Trazer as listas de cursos ofertados na unidade    
    [x] Trazer todos os endereços sociais (facebook, ...)  
    [x] Trazer todos as formas de contato (email, telefone e whatsapp)      
    [] Demanda dos cursos - criar relacionamento com o resultado
[x] Página escolha do curso
[] Página Detalhes Curso
    []...
[] Layout para exibir as demandas  
    []...
[] Lógica de Demanda (Resultados)

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
