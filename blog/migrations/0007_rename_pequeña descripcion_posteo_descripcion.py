# Generated by Django 4.0.1 on 2022-02-09 22:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_posteo_pequeña descripcion'),
    ]

    operations = [
        migrations.RenameField(
            model_name='posteo',
            old_name='Pequeña descripcion',
            new_name='descripcion',
        ),
    ]
