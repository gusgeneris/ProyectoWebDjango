# Generated by Django 4.0.1 on 2022-02-09 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_posteo_options_alter_posteo_contenido'),
    ]

    operations = [
        migrations.AddField(
            model_name='posteo',
            name='slug',
            field=models.CharField(blank=True, max_length=190, null=True),
        ),
    ]
