# Generated by Django 5.0.2 on 2024-02-26 09:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('algo', '0005_alter_problem_tags_ds_article'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='tag_algo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='algo.algorithm'),
        ),
        migrations.AlterField(
            model_name='article',
            name='tag_ds',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='algo.data_structure'),
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('url', models.URLField()),
                ('tag_algo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='algo.algorithm')),
                ('tag_ds', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='algo.data_structure')),
            ],
        ),
    ]
