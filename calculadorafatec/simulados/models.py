from django.db import models
from django.template.defaultfilters import slugify

class ProcessoSeletivoVestibularFatec(models.Model):
    ANALISE = 'AN'
    EXAME = 'EX'
    FORMATO_PROCESSO = [
        (ANALISE, 'Análise Histórico Escolar'),
        (EXAME, 'Exame'),    
    ]

    semestre = models.IntegerField(blank=True,null=True)
    ano  = models.IntegerField(blank=True,null=True)
    edicao =  models.CharField(verbose_name='edição',max_length=20, blank=True,null=True)    
    
    formato_processo = models.CharField(verbose_name='formato de seleção',
        max_length=2,
        choices=FORMATO_PROCESSO,
        default=EXAME,
    )  
    edital = models.FileField(upload_to="provas", blank=True,null=True) 
    data_prova = models.DateField('data do exame', blank=True, null=True)    
    link_prova = models.URLField(max_length=500, blank=True,null=True)
    prova = models.FileField(upload_to="provas", blank=True,null=True) 
    
    gabarito = models.FileField(upload_to="provas", blank=True,null=True) 
    total_vagas = models.IntegerField(verbose_name='total de vagas', blank=True,null=True)
    total_inscritos = models.IntegerField(verbose_name='total de inscritos', blank=True,null=True)
    qtde_questoes_anulada = models.IntegerField(verbose_name='quantidade de questões anuladas', blank=True,null=True)
    qtde_fatecs =  models.IntegerField(verbose_name='quantidade de fatecs no processo seletivo', blank=True,null=True)
    qtde_cursos = models.IntegerField(verbose_name='quantidade de cursos no processo seletivo', blank=True,null=True)
    simulado_gratuito = models.BooleanField('simulado gratuito',default=False)    
    slug = models.SlugField(unique=True, blank=True, null=True)        
    observacao = models.TextField("observação",  blank=True, null= True)
    criado_em = models.DateTimeField('criado em',auto_now=True)

    class Meta:
        verbose_name_plural = 'processos seletivos dos vestibulares da fatec'
        verbose_name = 'processo seletivo do vestibular da fatec'
        ordering = ('-semestre','-ano')
    
    def save(self, *args, **kwargs):
        if not self.edicao:
            self.edicao = f'{self.semestre}° semestre de {self.ano}'

        return super().save(*args, **kwargs)

    def __str__(self):
        return str(self.edicao)