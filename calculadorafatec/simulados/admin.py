from django.contrib import admin
from django.utils.html import format_html
from calculadorafatec.simulados.models import ProcessoSeletivoVestibularFatec

class ProcessoSeletivoVestibularFatecModelAdmin(admin.ModelAdmin):
    exclude = ['edicao']
    readonly_fields = ['edicao_']  
    prepopulated_fields = {'slug': ('semestre','ano'),}
    list_display = ['edicao_', 'formato_processo', 'edital', 'data_prova', 'prova_link','total_vagas','total_inscritos','simulado_gratuito','observacao']
    search_fields = ('edicao_','ano')
    list_filter = ('ano','simulado_gratuito')
    ordering = ('-ano','-semestre')

    def edicao_(self, obj):
        return obj.edicao

    edicao_.short_description = 'edição'      

    def prova_link(self, obj):        
        return format_html('<a href="{0}" target="_blank">{0}</a>', obj.link_prova)   
    
    prova_link.short_description = 'Prova'      


admin.site.register(ProcessoSeletivoVestibularFatec,ProcessoSeletivoVestibularFatecModelAdmin)