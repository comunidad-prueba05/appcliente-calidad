# Generated by Django 3.0.4 on 2020-11-06 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ordenes', '0002_cliente_ordengenerada'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordengenerada',
            name='estado',
            field=models.BooleanField(blank=True, default=True, null=True),
        ),
    ]