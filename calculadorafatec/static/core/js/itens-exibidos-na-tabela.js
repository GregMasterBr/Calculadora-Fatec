$(document).ready(function(){
    $("select[name='quantidades_cursos']").change(function(){
        select_itens_tabela = this.value;
        //mostrar_quantidade_itens_tabela(select_itens_tabela)
        // A hipotese é boa mas não funciona perfeitamente. Precisava de alguma maneira forçar o submit do form. Então simplifiquei e coloquei o onchange no select direto para submit do form.
    });

  });


  function mostrar_quantidade_itens_tabela(item){
    crsf_token = document.getElementsByName("csrfmiddlewaretoken");
    fetch("/materias-prova-peso2/?csrfmiddlewaretoken="+crsf_token[0].value+"&quantidades_cursos="+item,{
        method: "GET"        
    }).then(function(result){
        console.log(result)        
    }).catch(err => console.log(err.message))
  }

  function mostrar_quantidade_itens_tabela_POST(item){
    alert(item);
    //materias-prova-peso2
    crsf_token = document.getElementsByName("csrfmiddlewaretoken");
    data = new FormData();
    data.append('quantidades_cursos',item)

    fetch("/materias-prova-peso2/",{
        method: "POST",
        headers: {
            'X-CSRFToken':crsf_token[0].value
        },
        body: data
    }).then(function(result){
        console.log(result)
    }) 
  }