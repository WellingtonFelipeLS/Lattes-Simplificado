from django.db.models import Model
from django.db.models.fields import CharField, IntegerField, TextField

# Create your models here.

class LinhasDePesquisa(Model):
	detalhamento = CharField(max_length=50)

class ProjetosDePesquisa(Model):
	integrantes = CharField(max_length=200)
	anoDeInicio = IntegerField()
	anoDeTermino = IntegerField()
	titulo = CharField(max_length=200)
	descricao = TextField()
