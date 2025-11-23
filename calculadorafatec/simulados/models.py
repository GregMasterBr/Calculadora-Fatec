from django.db import models
from django.template.defaultfilters import slugify
from calculadorafatec.core.models import Disciplinas
from django.contrib.auth.models import User
from django.conf import settings
from django.utils import timezone

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
        
        if not self.slug:
            self.slug = slugify(self.edicao)
        
        return super().save(*args, **kwargs)

    def __str__(self):
        return str(self.edicao)
    
class Questao(models.Model):
    processo = models.ForeignKey(ProcessoSeletivoVestibularFatec,
        on_delete=models.CASCADE,
        related_name="questoes"
    )
    
    numero = models.IntegerField(blank=True, null=True)
    enunciado = models.TextField()
    imagem = models.ImageField(upload_to="questoes", blank=True, null=True)

    disciplina = models.ForeignKey(
        Disciplinas,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    anulada = models.BooleanField(default=False)
    criado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('processo', 'numero')
        ordering = ('numero',)

    def __str__(self):
        return f"Q{self.numero} - {self.processo.edicao or self.processo.slug or self.processo.ano}"



class Alternativa(models.Model):
    questao = models.ForeignKey(
        Questao, on_delete=models.CASCADE, related_name="alternativas"
    )
    letra = models.CharField(max_length=2, blank=True, null=True)
    texto = models.TextField()
    correta = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.letra} - Alternativa da Q{self.questao.numero}"


class SimuladoPersonalizado(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=200)
    descricao = models.TextField(blank=True, null=True)
    criado_em = models.DateTimeField(auto_now_add=True)

    questoes = models.ManyToManyField(Questao, blank=True, related_name="simulados_personalizados")
    total_questoes = models.IntegerField(blank=True, null=True)
    nota_maxima = models.FloatField(blank=True, null=True)
    tempo_limite_minutos = models.IntegerField(blank=True, null=True)
    publico = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.titulo} ({self.user})"
    

class TentativaSimulado(models.Model):
    simulado = models.ForeignKey(SimuladoPersonalizado, on_delete=models.CASCADE, related_name="tentativas")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    iniciado_em = models.DateTimeField(auto_now_add=True)
    finalizado_em = models.DateTimeField(blank=True, null=True)
    tempo_segundos = models.IntegerField(blank=True, null=True)

    nota_final = models.FloatField(blank=True, null=True)

    def calcular_nota(self):
        respostas = self.respostas.all()
        total_questoes = respostas.count()
        corretas = sum(1 for r in respostas if r.correta)
        if total_questoes:
            self.nota_final = round((corretas / total_questoes) * 100, 2)
        else:
            self.nota_final = 0
        return self.nota_final

    def finalizar(self):
        self.finalizado_em = timezone.now()
        self.tempo_segundos = int((self.finalizado_em - self.iniciado_em).total_seconds())
        self.calcular_nota()
        self.save()

    def __str__(self):
        return f"{self.user} - {self.simulado.titulo} - {self.nota_final}"


class RespostaDoUsuario(models.Model):
    tentativa = models.ForeignKey(TentativaSimulado, on_delete=models.CASCADE, related_name="respostas")
    questao = models.ForeignKey(Questao, on_delete=models.CASCADE)    
    alternativa_marcada = models.ForeignKey(Alternativa, on_delete=models.SET_NULL, null=True)

    correta = models.BooleanField(default=False)
    marcado_em = models.DateTimeField(auto_now_add=True)
    class Meta:
        unique_together = ('tentativa', 'questao')

    def save(self, *args, **kwargs):
        if self.alternativa_marcada:
            self.correta = self.alternativa_marcada.correta
        else:
            self.correta = False            
        super().save(*args, **kwargs)
        
    def __str__(self):
        return f"Resposta de {self.tentativa.user} para Q{self.questao.numero}"