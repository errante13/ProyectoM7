# Generated by Django 5.0.6 on 2024-07-21 07:12

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comuna',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Estado_solicitud',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombres', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Tipo_inmueble',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Tipo_usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Inmueble',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombres', models.CharField(max_length=50)),
                ('descripcion', models.TextField()),
                ('m2_construidos', models.FloatField()),
                ('m2_terreno', models.FloatField()),
                ('nun_estacionamientos', models.IntegerField(default=0)),
                ('num_habitaciones', models.IntegerField(default=0)),
                ('num_banos', models.IntegerField(default=0)),
                ('direccion', models.CharField(max_length=50)),
                ('precio_mensual', models.FloatField()),
                ('comuna', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='arriendo.comuna')),
                ('region', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='arriendo.region')),
                ('tipo_inmueble', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='arriendo.tipo_inmueble')),
            ],
        ),
        migrations.AddField(
            model_name='comuna',
            name='region',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='arriendo.region'),
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('rut', models.CharField(max_length=9, primary_key=True, serialize=False)),
                ('direccion', models.CharField(blank=True, max_length=50, null=True)),
                ('telefono', models.CharField(blank=True, max_length=50, null=True)),
                ('tipo_usuario', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='arriendo.tipo_usuario')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Solicitud',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_solicitud', models.DateField(auto_now_add=True)),
                ('estado', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='solicitudes', to='arriendo.estado_solicitud')),
                ('inmueble', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='solicitudes', to='arriendo.inmueble')),
                ('arrendatario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='solicitudes', to='arriendo.usuario')),
            ],
        ),
        migrations.AddField(
            model_name='inmueble',
            name='propietario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='arriendo.usuario'),
        ),
    ]
