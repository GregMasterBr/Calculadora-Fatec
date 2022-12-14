$(document).ready(function() {
    $('#CursoMateria').DataTable( {
        "ajax": {
            //"url": "https://calculadorafatec.gregmaster.com.br/calculadora/ajax/getTodosCursosMateriasPeso2.php",
            url: '../static/core/js/datamateriaspeso2.json',

            "dataSrc": ""
        },
        "columns": [
            { "data": "curso" },
            { "data": "materia_1" },
            { "data": "materia_2" }
        ],
        "language": {
            "lengthMenu": "Exibindo _MENU_ registros na página",
            "zeroRecords": "Nenhuma registro foi localizado",
            "info": "Exibindo _PAGE_ de _PAGES_ páginas",
            "infoEmpty": "Sem registros disponíveis",
            "infoFiltered": "(Filtrado _MAX_ do total de registros)",
            "loadingRecords": "Carregando...",
            "processing":     "Processando...",
            "search":         "Procurar curso:",
            "paginate": {
                "first":      "Primeiro",
                "last":       "Último",
                "next":       "Próximo",
                "previous":   "Anterior"
            }  
        }		        
    } );    
} );		