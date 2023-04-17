# Generated by Django 4.1.5 on 2023-04-16 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('curriculo', '0002_rename_imagem_pesquisador_foto'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='linhapesquisa',
            options={'verbose_name_plural': 'Linhas de Pesquisa'},
        ),
        migrations.AlterModelOptions(
            name='projetopesquisa',
            options={'verbose_name_plural': 'Prrojetos de Pesquisa'},
        ),
        migrations.AddField(
            model_name='pesquisador',
            name='telefone',
            field=models.CharField(default=79999999999, max_length=11),
            preserve_default=False,
        ),
    ]
