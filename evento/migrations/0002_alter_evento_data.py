# Generated by Django 5.1.2 on 2024-11-03 00:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("evento", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="evento",
            name="data",
            field=models.DateField(),
        ),
    ]
