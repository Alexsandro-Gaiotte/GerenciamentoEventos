# Generated by Django 5.1.2 on 2024-11-10 02:35

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("evento", "0007_alter_evento_slug"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name="evento",
            name="idCriador",
        ),
        migrations.AddField(
            model_name="evento",
            name="criador",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="eventos",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
