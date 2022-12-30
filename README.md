# Calculadora Fatec  
Construção da Plataforma Calculadora Fatec em versão **Python**.  
A versão desenvolvida em **PHP** pode ser vista em: <https://calculadorafatec.gregmaster.com.br/calculadora.html>

## A FAZER  
- [x] Estrutura base do projeto    
- [x] Rotas (Home e funcionalidades)     
- [x] Instalação do boostrap v5 no base.html    
- [x] Página da calculadora fatec - Home  
- [x] Página da ferramenta calculadora fatec  
    - [x] Replica do layout  
    - [x] Separado o conteúdo em includes  
    - [x] funcionalidade da lógica de cálculo via JS  
- [x] Página matérias de peso 2  
    - [x] Listagem das matérias de peso 2 por curso  
    - [x] Filtro de pesquisa por nome do curso 
    - [x] Filtro de pesquisa por eixo tecnologico  
    - [x] Criar o filtro de quantos itens serão exibidos na tabela  
        - [x] Lógica de onchange com o JS para fazer o fetch (itens-exibidos-na-tabela) e repassando para o python. O ciclo acontece mas o template não é atualizado. Desta maneira, é forçao um submit do form.
    - [x] Mecanimo de paginação dos resultados  
    - [x] Lógica para filtrar itens do pesquise por nome curso sem considerar a acentuação e capslock  (implementação unaccent lookup - precisa configuração e uso do postgres)
- [x] Página escolha da Instituição       
    - [x] Lógica para buscar e rederizar do ID para o Slug  
- [x] Página Detalhes Instituição  
    - [ ] Cadastrar informações da instituição  no BD
    - [x] Trazer as listas de cursos ofertados na unidade    
    - [x] Trazer todos os endereços sociais (facebook, ...)  
    - [x] Trazer todos as formas de contato (email, telefone e whatsapp)      
    - [x] Demanda dos cursos - criar relacionamento com o resultado para exibir tabela com  as demandas  
        - [x] Lógica de Demanda (Resultados)  
        - [x] Layout para exibir as demandas no template  
- [x] Página escolha do curso  
    - [x] Lógica para buscar e rederizar do ID para o Slug   
[/] Página Detalhes Curso  
    - [x] Adicionado os campos na model  
    - [ ] Cadastrar informações do curso  no BD
    - [x] Detalhes e informações sobre o curso  
    - [ ]  Trazer relação de cursos semelhantes que o aluno possa se interessar  
- [x] Página nota de corte    
    - [x] Página de seleção de dados - Consulta por Fatec e Fatec Curso. Lógica atribuída ao JS e rota no python  
    - [x] Página de detalhes dos dados considerando filtro enviado  
- [ ] Página de simulados   
    - [ ] Criar uma nova app  
    - [ ] Criar maneira de realizar um simulado
        - [ ] 
- [ ] Histórico  do Vestibular
    - [ ] Edição - Ano, Semestre, Data da prova, Formato (Prova, Análise de Histórico Escolar), Edital (arquivo), Prova(arquivo), Gabarito Prova (arquivo), Quantidade de questões anuladas, Quantidade de Inscritos, Quantidade de Vagas, Demanda, Quantas Fatecs, Quantos Cursos, 
- [ ] Provas do Vestibular    
    - [ ] Arquivo
    - [ ] Ano, Semestre
    - [ ] Banco de questões informatizadas (será usada para os simulados)
***
<br />

## Úteis para e sobre o projeto

Para fazer import via linha de comando do sqllite
* Baixar o executável: (sqlite3.exe)[https://www.sqlite.org/download.html] (sqlite-tools-win32-x86-3400000.zip)
https://www.youtube.com/watch?v=vs6dXL9Wp7s&t=243s

``` sheel
> .\sqlite3.exe .\db.sqlite3
sqlite> .mode csv
sqlite> .import arquivo_de_import.csv core_nome_da_tabela
        .import resultado_fatec_1_2015.csv core_resultadovestibularfatec
``` 

* https://django-import-export.readthedocs.io/en/latest/getting_started.html
* https://docs.djangoproject.com/en/2.2/ref/models/querysets/#select-related
* https://swapps.com/blog/quick-start-with-django-orm/
* https://docs.djangoproject.com/en/4.1/topics/db/managers/
*https://stackoverflow.com/questions/34904171/is-there-a-way-to-specify-the-order-of-creation-of-the-columns-for-an-sql-table  

Is there a way to specify the order of creation of the columns for an SQL table conception using Django?

``` python
class My_table(models.Model):
    field1 = models.CharField(primary_key=True, max_length=25)
    field2 = models.ForeignKey(....)
    field3 = models.IntegerField(blank=True, null=True)
    field4 = models.CharField(max_length=2000, blank=True, null=True)
```    
Can give a table like :

```html

  field1 | field3 | field4 | field2  
 --------+--------+--------+--------
```

I want this :

```html
  field1 | field2 | field3 | field4  
 --------+--------+--------+--------
```

Is there a way to have this result?

SOLVE:
POST MIGRATION
https://stackoverflow.com/questions/31698103/how-do-i-execute-raw-sql-in-a-django-migration


FIRST(), EXISTS(), GET() e GET_OBJECT_OR_404().  


* https://django-smart-selects.readthedocs.io/en/latest/  
