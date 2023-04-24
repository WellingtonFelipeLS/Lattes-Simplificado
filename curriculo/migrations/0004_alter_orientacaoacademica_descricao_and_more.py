# Generated by Django 4.1.5 on 2023-04-23 22:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('curriculo', '0003_remove_posgraduacao_area_de_pesquisa_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orientacaoacademica',
            name='descricao',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='orientacaoacademica',
            name='instituicao',
            field=models.CharField(default='', max_length=300),
        ),
        migrations.AlterField(
            model_name='orientacaoacademica',
            name='orientando',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='orientacaoacademica',
            name='tipo',
            field=models.IntegerField(choices=[(0, 'Iniciação Científica'), (1, 'TCC'), (2, 'Mestrado'), (3, 'Doutorado'), (4, 'Pós-Doutorado')], default=0),
        ),
        migrations.AlterField(
            model_name='premio',
            name='ano',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='premio',
            name='descricao',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='producaobibliografica',
            name='ano',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='producaobibliografica',
            name='autores',
            field=models.CharField(default='', max_length=300),
        ),
        migrations.AlterField(
            model_name='producaobibliografica',
            name='edicao',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='producaobibliografica',
            name='pagina_final',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='producaobibliografica',
            name='pagina_inicial',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='producaobibliografica',
            name='titulo',
            field=models.CharField(default='', max_length=300),
        ),
        migrations.AlterField(
            model_name='producaotecnica',
            name='ano',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='producaotecnica',
            name='autores',
            field=models.CharField(default='', max_length=300),
        ),
        migrations.AlterField(
            model_name='producaotecnica',
            name='titulo',
            field=models.CharField(default='', max_length=300),
        ),
        migrations.AlterField(
            model_name='proeficienciaidioma',
            name='compreensao',
            field=models.IntegerField(choices=[(0, 'Pouco'), (1, 'Razoavelmente'), (2, 'Bem')], default=0),
        ),
        migrations.AlterField(
            model_name='proeficienciaidioma',
            name='escrita',
            field=models.IntegerField(choices=[(0, 'Pouco'), (1, 'Razoavelmente'), (2, 'Bem')], default=0),
        ),
        migrations.AlterField(
            model_name='proeficienciaidioma',
            name='fala',
            field=models.IntegerField(choices=[(0, 'Pouco'), (1, 'Razoavelmente'), (2, 'Bem')], default=0),
        ),
        migrations.AlterField(
            model_name='proeficienciaidioma',
            name='leitura',
            field=models.IntegerField(choices=[(0, 'Pouco'), (1, 'Razoavelmente'), (2, 'Bem')], default=0),
        ),
    ]