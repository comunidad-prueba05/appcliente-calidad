# Generated by Django 3.0.4 on 2020-11-05 21:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ordenes', '0002_auto_20201105_1536'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicio',
            name='orden_generada',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='servicio',
            name='orden_transito',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]
