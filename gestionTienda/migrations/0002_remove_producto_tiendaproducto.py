# Generated by Django 4.2.3 on 2023-07-31 03:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestionTienda', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producto',
            name='tiendaProducto',
        ),
    ]
