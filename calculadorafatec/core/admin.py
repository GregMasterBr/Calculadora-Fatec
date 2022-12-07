from django.contrib import admin
from django.utils.html import format_html
from django.conf import settings
from calculadorafatec.core.models import Contact, Social, EixoTecnologico, Curso, Fatec, Regiao, ResultadoVestibularFatec,ResultadoVestibularFatec2

class CursoModelAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('curso',)}
    list_display = ['curso','eixo_tecnologico','conteudo_estudo','profissional_faz', 'mercado_trabalho', 'ativo']
    search_fields = ('curso',)
    list_filter = ('eixo_tecnologico','ativo')


class SocialInLine(admin.TabularInline):
    model = Social
    extra = 1
    #max_num = 1

class ContactInLine(admin.TabularInline):
    model = Contact
    extra = 1

class FatecModelAdmin(admin.ModelAdmin):
    inlines = [SocialInLine, ContactInLine]
    prepopulated_fields = {'slug': ('fatec','institucional')}

    list_display = ['fatec','imagem_fachada','institucional','cidade', 'regiao', 'email', 'phone','whatsapp','website_link']
    search_fields = ('fatec','institucional','cidade')

    def website_link(self, obj):
        link = obj.social_set.sites().first() if obj.social_set.sites() else ""
        return format_html('<a href="{0}" target="blank">{0}</a>', link)
    
    website_link.short_description = 'website'

    def imagem_fachada(self,obj):
        return format_html('<a href="{0}{1}" target="blank"><img width="60px" src="{0}{1}" alt="foto da fachada" /></a>', settings.MEDIA_URL,obj.imagem)
    
    imagem_fachada.allow_tags = True
    imagem_fachada.short_description = 'fachada'

    def email(self, obj):
        return obj.contact_set.emails().first()

    email.short_description = 'e-mail'

    def phone(self, obj):
        return obj.contact_set.phones().first()

    phone.short_description = 'telefone'    

    def whatsapp(self, obj):
        return obj.contact_set.whatsapps().first()

    whatsapp.short_description = 'whatsapp'        

class ResultadoVestibularFatecModelAdmin(admin.ModelAdmin):
    list_display = ['cod_resultado_fatec',	'cod_curso', 'cod_instituicao', 'ano', 'semestre', 'periodo', 'qtde_vagas', 'qtde_inscrito', 'demanda', 'nota_corte', 'nota_maxima']
    ordering = ('cod_resultado_fatec', 'semestre', 'ano')

admin.site.register(Fatec,FatecModelAdmin)
admin.site.register(Regiao)
admin.site.register(EixoTecnologico)
admin.site.register(Curso, CursoModelAdmin)
admin.site.register(ResultadoVestibularFatec, ResultadoVestibularFatecModelAdmin)
admin.site.register(ResultadoVestibularFatec2)
