# Generated by Django 4.0.3 on 2023-03-30 22:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animal', '0005_alter_animal_imagem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal',
            name='imagem',
            field=models.ImageField(null=True, upload_to='static/imagens/animal/'),
        ),
    ]
