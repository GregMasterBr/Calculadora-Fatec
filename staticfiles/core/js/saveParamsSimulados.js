function SalvarConstantesSimulado() {
    //https://www.treinaweb.com.br/blog/quando-usar-sessionstorage-e-localstorage/
    let curso_ = $("#cursos option:selected").val(); //ele~já está em array
    curso_ = curso_.split(" ");
    let vestibular_ = $("#vestibular option:selected").val();
    vestibular_ = vestibular_.split(" ");
  
    let configParams = JSON.stringify({
      ano   : vestibular_[1],
      semestre : vestibular_[0], 
      curso    : curso_[0],    
      peso1    : curso_[1],
      peso2    : curso_[2],
      code : $('body').attr('id')
    });
  
      localStorage.setItem("configParamsSimulado",configParams);
      //sessionStorage.setItem("configParamsSimulado",configParams);
  
  }