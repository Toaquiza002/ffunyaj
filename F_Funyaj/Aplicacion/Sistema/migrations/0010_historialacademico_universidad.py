# Generated by Django 5.0.8 on 2025-01-16 19:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Sistema', '0009_alter_actividaddevoluntariado_horas'),
    ]

    operations = [
        migrations.AddField(
            model_name='historialacademico',
            name='universidad',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='Sistema.universidad'),
        ),
    ]
