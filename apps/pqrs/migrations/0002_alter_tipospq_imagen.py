# Generated by Django 3.2.13 on 2023-02-26 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pqrs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tipospq',
            name='imagen',
            field=models.ImageField(upload_to='imagenes/tipospqs/%Y/%m/%d/'),
        ),
    ]
