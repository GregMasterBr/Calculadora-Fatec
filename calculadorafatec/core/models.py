from django.db import models
from django.template.defaultfilters import slugify
from calculadorafatec.core.managers import  KindQuerySet
from django.shortcuts import resolve_url as r
from .choices_disciplinas import ChoicesDisciplinas


# Create your models here.
class Regiao(models.Model):
    regiao = models.CharField(max_length=100) 
    
    def __str__(self):
        return self.regiao
       

class EixoTecnologico(models.Model):
    eixo_tecnologico = models.CharField(max_length=100, blank=True)
    
    def __str__(self):
        return self.eixo_tecnologico

class Curso(models.Model):
    #cod_curso = models.PositiveIntegerField(primary_key=True) or cod_curso = models.AutoField(primary_key=True)
    curso = models.CharField(max_length=100, blank=True)
    eixo_tecnologico = models.ForeignKey(EixoTecnologico, blank=True, null=True, on_delete=models.SET_NULL)
    materia_1 = models.CharField('Materia peso 2 (1ª)', blank=True, max_length=4, choices=ChoicesDisciplinas.choices)
    materia_2 = models.CharField('Materia peso 2 (2ª)', blank=True, max_length=4, choices=ChoicesDisciplinas.choices)    
    conteudo_estudo = models.TextField("O aluno estuda",  blank=True, null= True)
    profissional_faz = models.TextField("O profisisonal faz", blank=True, null= True)
    mercado_trabalho = models.TextField("Mercado de trabalho", blank=True, null= True)
    #sugestao_cursos = models.ManyToManyField(Curso)    
    ativo = models.BooleanField('ativa',default=True)
    slug = models.SlugField(unique=True, blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Cursos'
        verbose_name = 'Curso'
        ordering = ('curso',)

    #attributes
    @property
    def cod_curso(self):
        return self.id
        #access it as curso.cod_curso where you would normally do curso.id

    def __str__(self) -> str:
        return self.curso

class Fatec(models.Model):
    #cod_instituicao = models.PositiveIntegerField(primary_key=True) or cod_instituicao = models.AutoField(primary_key=True)
    fatec = models.CharField(max_length=100, unique=True)
    institucional = models.CharField(max_length=100, blank=True)
    regiao = models.ForeignKey(Regiao, on_delete=models.SET_NULL, null=True, verbose_name='região')
    cidade = models.CharField(max_length=100, blank=True)
    endereco = models.CharField(max_length=150, blank=True)
    googlemaps_iframe = models.TextField(blank=True, null= True)
    googlemaps = models.URLField(blank=True)
    site = models.URLField(blank=True)
    data_inauguracao = models.DateField('Data de Inauguração', blank=True, null=True)
    criado_em = models.DateTimeField('criado em',auto_now=True)
    ativo = models.BooleanField('ativa',default=True)
    slug = models.SlugField(unique=True, blank=True, null=True)
    cursos= models.ManyToManyField(Curso,  blank=True) 
    imagem = models.ImageField('Fachada',upload_to="fatecs",blank=True, null=True)
    #imagem = models.ForeignKey( Imagem, on_delete=models.SET_NULL, null=True, related_name='Imagem', blank=True)

    class Meta:
        verbose_name_plural = 'Fatecs'
        verbose_name = 'Fatec'
        ordering = ('fatec',)

    def __str__(self) -> str:
        return f"{self.fatec} {self.institucional}"


    def get_absolute_url(self):
            return r('detalhes_fatec', slug=self.slug)

    def qtd_cursos(self):
        return Curso.objects.filter(fatec__id=self.id).count()

    # def save(self, *args, **kwargs):
    #     if not self.slug:
    #         self.slug = slugify(self.fatec)
    #    return super().save(*args, **kwargs)        


class Contact(models.Model):
    EMAIL = 'E'
    PHONE = 'P'
    WHATSAPP = 'W'

    KINDS=(
        (EMAIL,'Email'),
        (PHONE,'Telefone'),
        (WHATSAPP,'Whatsapp'),
    )
    
    Fatec = models.ForeignKey('Fatec', on_delete=models.CASCADE, verbose_name='Fatec')
    kind = models.CharField('tipo', max_length=1, choices=KINDS)
    value = models.CharField('valor', max_length=255)

    objects = KindQuerySet.as_manager()
    class Meta:
        verbose_name_plural = 'contatos'
        verbose_name = 'contato'
    
    def __str__(self):
        return self.value  

class Social(models.Model):
    SITE = 'W'
    FACEBOOK = 'F'
    INSTAGRAM = 'I'
    YOUTUBE = 'Y'
    LINKEDIN = 'L'
    TWITTER = 'T'
    BLOG = 'B'
    OUTROS = 'O'

    KINDS=(
        (SITE,'Site'),
        (FACEBOOK,'Facebook'),
        (INSTAGRAM, 'Instagram'),
        (YOUTUBE, 'Youtube'),
        (LINKEDIN, 'Linkedin'),
        (TWITTER, 'Twitter'),        
        (BLOG, 'Blog'),
        (OUTROS,'Outros'),
    )
    
    Fatec = models.ForeignKey('Fatec', on_delete=models.CASCADE, verbose_name='Fatec')
    kind = models.CharField('tipo', max_length=1, choices=KINDS)
    value = models.CharField('valor', max_length=255)

    objects = KindQuerySet.as_manager()
    class Meta:
        verbose_name_plural = 'enderecos sociais'
        verbose_name = 'endereço social'
    
    def __str__(self):
        return self.value  


class ResultadoVestibularFatec(models.Model):
    cod_resultado_fatec = models.PositiveIntegerField(primary_key=True) 
    cod_curso = models.IntegerField()
    cod_instituicao = models.IntegerField()
    #cod_curso = models.ForeignKey(Curso, on_delete=models.SET_NULL, blank=True,null=True,)
    #cod_instituicao = models.ForeignKey(Fatec, on_delete=models.SET_NULL, blank=True,null=True,)
    ano = models.IntegerField()
    semestre = models.IntegerField()
    periodo = models.CharField(max_length=10)
    qtde_vagas = models.IntegerField()
    qtde_inscrito = models.IntegerField()
    demanda = models.FloatField()
    nota_corte = models.FloatField()
    nota_maxima = models.FloatField()

    class Meta:
        verbose_name_plural = 'resultados do vestibulares da fatec'
        verbose_name = 'resultado do vestibular da fatec'
    
    def nome_curso(self, id_ = 1): #teste
        cTeste = (Curso.objects.filter(id=id_).values('curso'))                
        return (Curso.objects.values('curso').get(pk=id_))        

    def __str__(self):
        return str(self.cod_resultado_fatec)