from django.db import models

class Premio(models.Model):
	ano = models.IntegerField()
	descricao = models.TextField()

	def __str__(self):
		return str(self.ano)

class LinhaPesquisa(models.Model):
	detalhamento = models.TextField()

	def __str__(self):
		return self.detalhamento

class ProducaoBibliografica(models.Model):
	titulo = models.CharField(max_length=300)
	autores = models.TextField()
	pagina_inicial = models.IntegerField()
	pagina_final = models.IntegerField()
	edicao = models.CharField(max_length=100)
	ano = models.IntegerField()

	def __str__(self):
		return self.titulo

# 0 - Pouco, 1 - Razoalvemente, 2 - Bem
class ProeficienciaIdioma(models.Model):
	idioma = models.CharField(max_length=100)
	compreensao = models.IntegerField()
	fala = models.IntegerField()
	escrita = models.IntegerField()
	leitura = models.IntegerField()

	def __str__(self):
		return self.idioma

class ProducaoTecnica(models.Model):
	titulo = models.CharField(max_length=300)
	autores = models.TextField()
	ano = models.IntegerField()

	def __str__(self):
		return self.titulo

# 0 - Iniciação Científica, 1 - TCC
# 2 - Mestrado, 3 - Doutorado, 4 - Pos-doutorado
class OrientacaoAcademica(models.Model):
	orientando = models.CharField(max_length=200)
	tipo = models.IntegerField()
	instituicao = models.CharField(max_length=300)
	descricao = models.TextField()

	def __str__(self):
		return self.instituicao

class AtuacaoProfissional(models.Model):
	ano_inicio = models.IntegerField()
	ano_termino = models.IntegerField()
	instituicao = models.CharField(max_length=300)
	vinculo = models.CharField(max_length=100)
	enquad_profissional = models.CharField(max_length=200)
	regime = models.CharField(max_length=100)

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
	nome = models.CharField(max_length=200)
	endereco = models.OneToOneField(EnderecoProfissional,on_delete=models.CASCADE)
	cpf = models.CharField(max_length=11)
	email = models.EmailField()
	foto = models.TextField()

	def __str__(self):
		return self.nome

class Graduacao(models.Model):
	titulo = models.CharField(max_length=200)
	orientador = models.CharField(max_length=200)
	notaConclusao = models.FloatField()
	palavrasChave = models.CharField(max_length=500)

	def __str__(self):
		return self.titulo

class AreaPesquisa(models.Model):
	area = models.CharField(max_length=200)
	grande_area = models.CharField(max_length=200)
	sub_area = models.CharField(max_length=200)
	especialidade_area = models.CharField(max_length=200)

class PosGraduacao(models.Model):
	titulo = models.CharField(max_length=200)
	orientador = models.CharField(max_length=200)
	palavrasChave = models.CharField(max_length=500)
	area_pesquisa = models.ForeignKey(
		AreaPesquisa,
		on_delete=models.CASCADE)
	
	def __str__(self):
		return self.titulo

class ProjetoPesquisa(models.Model):
    integrantes = models.TextField()
    titulo = models.CharField(max_length=200)
    ano_inicio = models.IntegerField()
    ano_termino = models.IntegerField()
    descricao = models.TextField()
    situacao = models.CharField(max_length=100)

    def __str__(self):
        return self.titulo


class Curriculo(models.Model):
    premios = models.ForeignKey(
        Premio,
		on_delete=models.CASCADE
    )
    producoesBibliograficas = models.ForeignKey(
        ProducaoBibliografica,
		on_delete=models.CASCADE
    )
    proficienciaIdiomas = models.ForeignKey(
        ProeficienciaIdioma,
		on_delete=models.CASCADE
    )
    producoesTecnicas = models.ForeignKey(
        ProducaoTecnica,
		on_delete=models.CASCADE
    )
    orientacoesAcademicas = models.ForeignKey(
        OrientacaoAcademica,
		on_delete=models.CASCADE
    )
    graduacoes = models.ForeignKey(
        Graduacao,
		on_delete=models.CASCADE
    )
    pos_graduacoes = models.ForeignKey(
        PosGraduacao,
		on_delete=models.CASCADE
    )
    atuacoes_profissionais = models.ForeignKey(
        AtuacaoProfissional,
		on_delete=models.CASCADE
    )
    graduacoes = models.ForeignKey(
        Graduacao,
		on_delete=models.CASCADE
    )
    projeto_pesquisa = models.ForeignKey(
        ProjetoPesquisa,
        on_delete=models.CASCADE
    )
    pesquisador = models.OneToOneField(
        Pesquisador,
        on_delete=models.CASCADE
    )