# Generated by Django 4.1.5 on 2023-04-23 16:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('curriculo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posgraduacao',
            name='area_de_pesquisa',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='curriculo.areapesquisa'),
        ),
    ]