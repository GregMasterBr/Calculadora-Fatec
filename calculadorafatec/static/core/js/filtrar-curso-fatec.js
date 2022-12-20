$(document).ready(function(){
    $("select[name='cod_fatec']").change(function(){
        select_fatec = this.value;
        select_curso = $("select[name='cod_curso']");                
        if (select_fatec > 0){
            select_curso.prop('disabled', false);
            busca_cursos_da_fatec(select_fatec);

        }else{
            select_curso.prop("selectedIndex", 0);
            select_curso.prop('disabled', 'disabled');            
        }
    });

  });


function busca_cursos_da_fatec(fatec){
    crsf_token = document.getElementsByName("csrfmiddlewaretoken");
    data = new FormData();
    data.append('fatec_id',fatec)
    select_curso = $("select[name='cod_curso']");    
    select_curso.empty();
    let option_ = new Option("Escolha um curso...", 0);
    select_curso.append(option_);

    fetch("/busca-cursos-da-fatec/",{
        method: "POST",
        headers: {
            'X-CSRFToken':crsf_token[0].value
        },
        body: data
    }).then(function(result){
        return result.json()
    }).then(function(data){
        console.log(data);
        cursos = data.cursos
        cursos.forEach(function(item){
            console.log(item, item.id, item.curso);
            let option = new Option(item.curso, item.id);
            //console.log(option);
            select_curso.append(option);
        });
    });

}

