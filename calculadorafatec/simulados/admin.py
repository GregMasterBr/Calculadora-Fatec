from django.contrib import admin
from django.utils.html import format_html
from calculadorafatec.simulados.models import  (
    ProcessoSeletivoVestibularFatec,
    Questao,
    Alternativa,
    SimuladoPersonalizado,
    TentativaSimulado,
    RespostaDoUsuario
)

class AlternativaInline(admin.TabularInline):
    model = Alternativa
    extra = 5

class QuestaoInline(admin.StackedInline):
    model = Questao
    extra = 10
    inlines = [AlternativaInline]


@admin.register(ProcessoSeletivoVestibularFatec)
class ProcessoSeletivoVestibularFatecModelAdmin(admin.ModelAdmin):
    exclude = ['edicao']
    readonly_fields = ['edicao_']
    prepopulated_fields = {'slug': ('semestre','ano'),}
    list_display = ['edicao_', 'formato_processo', 'edital', 'data_prova', 'prova_link',
                    'total_vagas','total_inscritos','simulado_gratuito','observacao']
    search_fields = ('edicao_','ano')
    list_filter = ('ano','simulado_gratuito')
    ordering = ('-ano','-semestre')
    inlines = [QuestaoInline]   # 👈 Inline aqui!

    def edicao_(self, obj):
        return obj.edicao
    edicao_.short_description = 'edição'

    def prova_link(self, obj):
        if obj.link_prova:
            return format_html('<a href="{0}" target="_blank">{0}</a>', obj.link_prova)
        return "-"
    prova_link.short_description = 'Prova'
    


@admin.register(Questao)
class QuestaoAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'disciplina', 'anulada')
    list_filter = ('disciplina', 'anulada')
    search_fields = ('enunciado',)
    inlines = [AlternativaInline]

@admin.register(SimuladoPersonalizado)
class SimuladoPersonalizadoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'user', 'criado_em')
    filter_horizontal = ('questoes',)

@admin.register(TentativaSimulado)
class TentativaAdmin(admin.ModelAdmin):
    list_display = ('simulado', 'user', 'nota_final', 'iniciado_em', 'finalizado_em')

@admin.register(RespostaDoUsuario)
class RespostaAdmin(admin.ModelAdmin):
    list_display = ('tentativa','questao','alternativa_marcada','correta')