from django.db import models
from django.contrib.auth.models import User

class Curriculo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    resumo = models.TextField()

class Premio(models.Model):
    ano = models.IntegerField(default=0)
    descricao = models.TextField(default='')
    curriculo = models.ForeignKey(Curriculo, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.ano)

class LinhaPesquisa(models.Model):
    detalhamento = models.CharField(max_length=150)
    curriculo = models.ForeignKey(Curriculo, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.detalhamento
    
    class Meta:
        verbose_name_plural = "Linhas de Pesquisa"

class ProducaoBibliografica(models.Model):
    titulo = models.CharField(max_length=300, default='')
    autores = models.CharField(max_length=300, default='')
    pagina_inicial = models.IntegerField(default=0)
    pagina_final = models.IntegerField(default=0)
    edicao = models.CharField(max_length=100,  default='')
    ano = models.IntegerField(default=0)
    curriculo = models.ForeignKey(Curriculo, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo

class ProeficienciaIdioma(models.Model):
    NivelProeficiencia = (
        (0, "Pouco"),
        (1, "Razoavelmente"),
        (2, "Bem")
    )
    idioma = models.CharField(max_length=100)
    compreensao = models.IntegerField(choices=NivelProeficiencia, default=0)
    fala = models.IntegerField(choices=NivelProeficiencia, default=0)
    escrita = models.IntegerField(choices=NivelProeficiencia, default=0)
    leitura = models.IntegerField(choices=NivelProeficiencia, default=0)
    curriculo = models.ForeignKey(Curriculo, on_delete=models.CASCADE)

    def __str__(self):
        return self.idioma

class ProducaoTecnica(models.Model):
    titulo = models.CharField(max_length=300, default='')
    autores = models.CharField(max_length=300,default='')
    ano = models.IntegerField(default=0)
    curriculo = models.ForeignKey(Curriculo, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo

class OrientacaoAcademica(models.Model):
    TipoOrientacao = (
        (0, "Iniciação Científica"),
        (1, "TCC"),
        (2, "Mestrado"),
        (3, "Doutorado"),
        (4, "Pós-Doutorado")
    )
    orientando = models.CharField(max_length=200, default='')
    tipo = models.IntegerField(choices=TipoOrientacao, default=0)
    instituicao = models.CharField(max_length=300, default='')
    descricao = models.TextField(default='')
    curriculo = models.ForeignKey(Curriculo, on_delete=models.CASCADE)

    def __str__(self):
        return self.instituicao

class AtuacaoProfissional(models.Model):
    ano_de_inicio = models.IntegerField(default=0)
    ano_de_termino = models.IntegerField(default=0)
    instituicao = models.CharField(max_length=300, default='')
    vinculo = models.CharField(max_length=100, default='')
    enquad_profissional = models.CharField(max_length=200, default='')
    regime = models.CharField(max_length=100, default='')
    curriculo = models.ForeignKey(Curriculo, on_delete=models.CASCADE)

    def __str__(self):
        return self.enquad_profissional

class EnderecoProfissional(models.Model):
    logradouro = models.CharField(max_length=200)
    bairro = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=100)

    def __str__(self):
        return self.logradouro

class Pesquisador(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    nome = models.CharField(max_length=200)
    endereco = models.OneToOneField(EnderecoProfissional, on_delete=models.CASCADE)
    cpf = models.CharField(max_length=11)
    telefone = models.CharField(max_length=11)
    email = models.EmailField()
    foto = models.ImageField('photos')

    def __str__(self):
        return self.nome

class FormacaoAcademica(models.Model):
    ano_de_inicio = models.IntegerField(default=0)
    ano_de_termino = models.IntegerField(default=0)
    nome = models.CharField(max_length=200, default='')
    instituicao = models.CharField(max_length=200, default='')
    curriculo = models.ForeignKey(Curriculo, on_delete=models.CASCADE)

    class Meta:
        abstract = True

class Graduacao(FormacaoAcademica):
    pass

class PosGraduacao(FormacaoAcademica):
    titulo = models.CharField(max_length=200, default='')
    orientador = models.CharField(max_length=200, default='')
    palavras_chave = models.CharField(max_length=500, default='')
    area = models.CharField(max_length=200, default='')
    grande_area = models.CharField(max_length=200, default='')
    sub_area = models.CharField(max_length=200, default='')
    especialidade_area = models.CharField(max_length=200, default='')
    
    def __str__(self):
        return self.titulo

class ProjetoPesquisa(models.Model):
    integrantes = models.TextField(default='')
    titulo = models.CharField(max_length=200, default='')
    ano_de_inicio = models.IntegerField(default=0)
    ano_de_termino = models.IntegerField(default=0)
    descricao = models.TextField(default='')
    situacao = models.CharField(max_length=100, default='')
    curriculo = models.ForeignKey(Curriculo, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo
    
    class Meta:
        verbose_name_plural = "Projetos de Pesquisa"