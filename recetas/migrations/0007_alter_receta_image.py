# Generated by Django 4.0.5 on 2022-07-04 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recetas', '0006_alter_receta_options_receta_porciones'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receta',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='recetas'),
        ),
    ]