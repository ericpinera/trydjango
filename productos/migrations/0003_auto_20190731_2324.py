# Generated by Django 2.0.7 on 2019-08-01 04:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0002_producto_caracteristicas'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='caracteristicas',
            field=models.BooleanField(default=False),
        ),
    ]
