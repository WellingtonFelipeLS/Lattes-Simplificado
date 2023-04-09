from django.contrib import admin
from .models import ProducaoBibliografica, LinhaPesquisa, ProjetoPesquisa

admin.site.register(ProducaoBibliografica)
admin.site.register(LinhaPesquisa)
admin.site.register(ProjetoPesquisa)