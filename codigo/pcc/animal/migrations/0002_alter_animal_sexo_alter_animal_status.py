# Generated by Django 4.0.3 on 2023-02-13 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animal', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal',
            name='sexo',
            field=models.CharField(choices=[('M', 'Macho'), ('F', 'Fêmea')], max_length=10),
        ),
        migrations.AlterField(
            model_name='animal',
            name='status',
            field=models.CharField(choices=[('Adotado', 'Adotado'), ('Nao_adotado', 'Não Adotado')], max_length=50),
        ),
    ]
