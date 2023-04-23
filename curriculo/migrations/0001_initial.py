# Generated by Django 4.1.5 on 2023-04-23 16:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='AreaPesquisa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area', models.CharField(default='', max_length=200)),
                ('grande_area', models.CharField(default='', max_length=200)),
                ('sub_area', models.CharField(default='', max_length=200)),
                ('especialidade_area', models.CharField(default='', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Curriculo',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('resumo', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='EnderecoProfissional',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logradouro', models.CharField(max_length=200)),
                ('bairro', models.CharField(max_length=100)),
                ('cidade', models.CharField(max_length=100)),
                ('estado', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ProjetoPesquisa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('integrantes', models.TextField()),
                ('titulo', models.CharField(max_length=200)),
                ('ano_de_inicio', models.IntegerField()),
                ('ano_de_termino', models.IntegerField()),
                ('descricao', models.TextField()),
                ('situacao', models.CharField(max_length=100)),
                ('curriculo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='curriculo.curriculo')),
            ],
            options={
                'verbose_name_plural': 'Projetos de Pesquisa',
            },
        ),
        migrations.CreateModel(
            name='ProeficienciaIdioma',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idioma', models.CharField(max_length=100)),
                ('compreensao', models.IntegerField(choices=[(0, 'Pouco'), (1, 'Razoavelmente'), (2, 'Bem')])),
                ('fala', models.IntegerField(choices=[(0, 'Pouco'), (1, 'Razoavelmente'), (2, 'Bem')])),
                ('escrita', models.IntegerField(choices=[(0, 'Pouco'), (1, 'Razoavelmente'), (2, 'Bem')])),
                ('leitura', models.IntegerField(choices=[(0, 'Pouco'), (1, 'Razoavelmente'), (2, 'Bem')])),
                ('curriculo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='curriculo.curriculo')),
            ],
        ),
        migrations.CreateModel(
            name='ProducaoTecnica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=300)),
                ('autores', models.TextField()),
                ('ano', models.IntegerField()),
                ('curriculo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='curriculo.curriculo')),
            ],
        ),
        migrations.CreateModel(
            name='ProducaoBibliografica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=300)),
                ('autores', models.TextField()),
                ('pagina_inicial', models.IntegerField()),
                ('pagina_final', models.IntegerField()),
                ('edicao', models.CharField(max_length=100)),
                ('ano', models.IntegerField()),
                ('curriculo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='curriculo.curriculo')),
            ],
        ),
        migrations.CreateModel(
            name='Premio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ano', models.IntegerField()),
                ('descricao', models.TextField()),
                ('curriculo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='curriculo.curriculo')),
            ],
        ),
        migrations.CreateModel(
            name='PosGraduacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ano_de_inicio', models.IntegerField(default=0)),
                ('ano_de_termino', models.IntegerField(default=0)),
                ('nome', models.CharField(default='', max_length=200)),
                ('instituicao', models.CharField(default='', max_length=200)),
                ('titulo', models.CharField(default='', max_length=200)),
                ('orientador', models.CharField(default='', max_length=200)),
                ('palavras_chave', models.CharField(default='', max_length=500)),
                ('area_de_pesquisa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='curriculo.areapesquisa')),
                ('curriculo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='curriculo.curriculo')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Pesquisador',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('nome', models.CharField(max_length=200)),
                ('cpf', models.CharField(max_length=11)),
                ('telefone', models.CharField(max_length=11)),
                ('email', models.EmailField(max_length=254)),
                ('foto', models.CharField(max_length=200)),
                ('endereco', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='curriculo.enderecoprofissional')),
            ],
        ),
        migrations.CreateModel(
            name='OrientacaoAcademica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orientando', models.CharField(max_length=200)),
                ('tipo', models.IntegerField(choices=[(0, 'Iniciação Científica'), (1, 'TCC'), (2, 'Mestrado'), (3, 'Doutorado'), (4, 'Pós-Doutorado')])),
                ('instituicao', models.CharField(max_length=300)),
                ('descricao', models.TextField()),
                ('curriculo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='curriculo.curriculo')),
            ],
        ),
        migrations.CreateModel(
            name='LinhaPesquisa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('detalhamento', models.CharField(max_length=150)),
                ('curriculo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='curriculo.curriculo')),
            ],
            options={
                'verbose_name_plural': 'Linhas de Pesquisa',
            },
        ),
        migrations.CreateModel(
            name='Graduacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ano_de_inicio', models.IntegerField(default=0)),
                ('ano_de_termino', models.IntegerField(default=0)),
                ('nome', models.CharField(default='', max_length=200)),
                ('instituicao', models.CharField(default='', max_length=200)),
                ('curriculo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='curriculo.curriculo')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AtuacaoProfissional',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ano_de_inicio', models.IntegerField()),
                ('ano_de_termino', models.IntegerField()),
                ('instituicao', models.CharField(max_length=300)),
                ('vinculo', models.CharField(max_length=100)),
                ('enquad_profissional', models.CharField(max_length=200)),
                ('regime', models.CharField(max_length=100)),
                ('curriculo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='curriculo.curriculo')),
            ],
        ),
    ]
