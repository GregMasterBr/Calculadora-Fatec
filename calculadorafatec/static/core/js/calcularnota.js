
	    function CalcularNota(){
            qpeso1();
            qpeso2();
            VerificarRedacao();	
            VerificarEnem();	

            let NPC = 0;
            let P = 0;
            let NotaEnem = 0;
            let N = 0;
            let NF = 0;
            let resultado;

            let q1=document.getElementById("q1").value;
            let q2=document.getElementById("q2").value;
            let redacao= document.getElementById("redacao").value;
            let nota_enem=0;
            let afro=document.getElementById("afro").checked;
            let publica= document.getElementById("publica").checked;

            NPC = parseInt((q2 * 2)) + parseInt(q1);
            P = (NPC * 100) / 64; 
            if (document.getElementById("ckdEnem").checked) {
                    let nota_enem = document.getElementById("nota_enem").value;
                    NotaEnem = nota_enem / 10;
                    if (NotaEnem > P) {
                        N = (4 * P + 1 * (NotaEnem)) / 5;
                    } else {
                        N = P;
                    }	       		 
            }else{
                N = P;
            }

            NF = (8 * N + 2 * redacao) / 10;
            resultado = NF;

            //Pontuação acrescida
            if (afro == true && publica == false) {
                resultado = resultado * 1.03;
            }
            if (afro== false && publica== true) {
                resultado = resultado * 1.1;
            }
            if (afro== true && publica == true) {
                resultado = resultado * 1.13;
            }

            if(resultado>100){
                resultado=100;
            }	       
            if ((resultado)) {
                document.getElementById("resultado").value=resultado;
            }else{
                alert("Por favor, preencher as informações que são necessárias para realizar o cálculo");
            }
	    }
        
	    function qpeso1(){
	    	let q1=document.getElementById("q1").value;
	    	if (q1>44) {
	    		alert("O máximo de acertos de questões de peso 1 é 44.");
	    		document.getElementById("q1").value='';
	    		//document.getElementById("q1").focus();
	    	}else{
	    		//document.getElementById("q2").focus();
	    	}
	    }	    

	    function qpeso2(){
	    	let q2=document.getElementById("q2").value;
	    	if (q2>10) {
	    		alert("O máximo de acertos de questões de peso 2 é 10.");
	    		document.getElementById("q2").value='';
	    		//document.getElementById("q2").focus();
	    	}else{
	    		//document.getElementById("redacao").focus();
	    	}
	    }
	    
	    function VerificarRedacao(){
	    	let redacao=document.getElementById("redacao").value;
	    	if (redacao>100) {
	    		alert("A nota máxima possível na redação é 100 pontos.");
	    		document.getElementById("redacao").value='';
	    		//document.getElementById("redacao").focus();
	    	}else{
	    		//document.getElementById("ckdEnem").focus();
	    	}
	    }	    

	    function VerificarEnem(){
			if (document.getElementById("ckdEnem").checked) {
	       		let nota_enem = document.getElementById("nota_enem").value;	   
	       		if (nota_enem<200 || nota_enem>1000) {
	       			alert("A nota aceita do ENEM é entre 200 e 1000 pontos.");
	       			document.getElementById("ckdEnem").checked = false;
	       			document.getElementById("nota_enem").value= '';
	       			document.getElementById("nota_enem").disabled=true;
	       		} 	
	    	}else{
	    		//document.getElementById("afro").focus();
	    	}	
	    } 

        function EnableDisableEnem(ckdEnem) {
            var txtNotaEnem = document.getElementById("nota_enem");
            txtNotaEnem.disabled = ckdEnem.checked ? false : true;
             if (!txtNotaEnem.disabled) {
                 txtNotaEnem.focus();
             }else{
                txtNotaEnem.value='';
             }
         }