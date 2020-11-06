# Generated by Django 3.0.4 on 2020-11-06 17:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ordenes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrdenGenerada',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_creation', models.DateTimeField(auto_now_add=True, null=True)),
                ('date_updated', models.DateTimeField(auto_now=True, null=True)),
                ('estado', models.BooleanField(default=True)),
                ('nombre', models.CharField(max_length=200, verbose_name='nombre cliente')),
                ('no_servicio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ordenes.Servicio')),
                ('user_creation', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ordenes_ordengenerada_creation', to=settings.AUTH_USER_MODEL)),
                ('user_updated', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ordenes_ordengenerada_updated', to=settings.AUTH_USER_MODEL)),
                ('username', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Orden registrada',
                'verbose_name_plural': 'Ordenes registradas',
                'db_table': 'orden_registrada',
            },
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_creation', models.DateTimeField(auto_now_add=True, null=True)),
                ('date_updated', models.DateTimeField(auto_now=True, null=True)),
                ('nombres', models.CharField(max_length=200, verbose_name='Nombres cliente')),
                ('apellidos', models.CharField(max_length=200, verbose_name='Apellidos cliente')),
                ('nit', models.CharField(max_length=20, verbose_name='NIT')),
                ('tel', models.CharField(max_length=10, verbose_name='telefono')),
                ('user_creation', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ordenes_cliente_creation', to=settings.AUTH_USER_MODEL)),
                ('user_updated', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ordenes_cliente_updated', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Cliente',
                'verbose_name_plural': 'Clientes',
                'db_table': 'cliente',
            },
        ),
    ]
