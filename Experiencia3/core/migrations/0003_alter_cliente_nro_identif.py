# Generated by Django 4.1.5 on 2023-01-22 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_rename_rut_cliente_nro_identif'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='nro_identif',
            field=models.CharField(max_length=15, primary_key=True, serialize=False, verbose_name='Rut'),
        ),
    ]
