# Generated by Django 4.2.2 on 2023-07-15 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0005_estudiantes_apellido'),
    ]

    operations = [
        migrations.AddField(
            model_name='estudiantes',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='imagenes'),
        ),
    ]