# Generated by Django 4.0.1 on 2022-02-06 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppServicios', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicios',
            name='imagen',
            field=models.ImageField(upload_to='servicios'),
        ),
    ]