# Generated by Django 5.0.2 on 2024-02-26 04:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('algo', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Algo_themes',
            new_name='Algo_theme',
        ),
        migrations.RenameModel(
            old_name='Data_structures_themes',
            new_name='Data_structures_theme',
        ),
    ]