# Generated by Django 4.1.5 on 2023-04-24 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('curriculo', '0004_alter_orientacaoacademica_descricao_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pesquisador',
            name='foto',
            field=models.ImageField(upload_to='', verbose_name='photos'),
        ),
    ]
