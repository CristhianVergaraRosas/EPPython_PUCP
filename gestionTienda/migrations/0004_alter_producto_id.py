# Generated by Django 4.2.3 on 2023-08-02 02:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionTienda', '0003_producto_tiendaproducto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
