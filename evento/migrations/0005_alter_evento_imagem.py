# Generated by Django 5.1.2 on 2024-11-03 22:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("evento", "0004_evento_imagem"),
    ]

    operations = [
        migrations.AlterField(
            model_name="evento",
            name="imagem",
            field=models.ImageField(blank=True, null=True, upload_to="imagens/"),
        ),
    ]
