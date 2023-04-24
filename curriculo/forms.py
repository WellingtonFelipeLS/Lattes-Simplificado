from typing import Any
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm, EmailField, ImageField, FileInput
from .models import *

class NewUserForm(UserCreationForm):
    email = EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

class PesquisadorForm(ModelForm):
    foto = ImageField(widget=FileInput)
    
    class Meta:
        model = Pesquisador
        fields = ["nome", "email", "telefone", "cpf", "foto"]

class CurriculoForm(ModelForm):
    class Meta:
        model = Curriculo
        fields = ['resumo']

class PremioForm(ModelForm):
    class Meta:
        model = Premio
        fields = ['ano', 'descricao']

class LinhaPesquisaForm(ModelForm):
    class Meta:
        model = LinhaPesquisa
        fields = ['detalhamento']

class ProducaoBibliograficaForm(ModelForm):
    class Meta:
        model = ProducaoBibliografica
        fields = ['titulo', 'autores', 'pagina_inicial', 'pagina_final', 'edicao', 'ano']

class ProeficienciaIdiomaForm(ModelForm):
    class Meta:
        model = ProeficienciaIdioma
        fields = ['idioma', 'compreensao', 'fala', 'escrita', 'leitura']

class ProducaoTecnicaForm(ModelForm):
    class Meta:
        model = ProducaoTecnica
        fields = ['titulo', 'autores', 'ano']

class OrientacaoAcademicaForm(ModelForm):
    class Meta:
        model = OrientacaoAcademica
        fields = ['orientando', 'tipo', 'instituicao', 'descricao']

class AtuacaoProfissionalForm(ModelForm):
    class Meta:
        model = AtuacaoProfissional
        fields = ['ano_de_inicio', 'ano_de_termino', 'instituicao', 'vinculo', 'enquad_profissional', 'regime']

class EnderecoProfissionalForm(ModelForm):
    class Meta:
        model = EnderecoProfissional
        fields = ['logradouro', 'bairro', 'cidade', 'estado']

class PesquisadorForm(ModelForm):
    class Meta:
        model = Pesquisador
        fields = ['nome', 'cpf', 'telefone', 'email', 'foto']

class GraduacaoForm(ModelForm):
    class Meta:
        model = Graduacao
        fields = ['ano_de_inicio', 'ano_de_termino', 'nome', 'instituicao'] 

class PosGraduacaoForm(ModelForm):          
    class Meta:
        model = PosGraduacao
        fields = ['ano_de_inicio', 'ano_de_termino', 'nome', 'instituicao', 'titulo', 'orientador', 'palavras_chave', 'area', 'grande_area', 'sub_area', 'especialidade_area']

class ProjetoPesquisaForm(ModelForm):
    class Meta:
        model = ProjetoPesquisa
        fields = ['integrantes', 'titulo', 'ano_de_inicio', 'ano_de_termino', 'descricao', 'situacao']
