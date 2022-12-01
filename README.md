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

