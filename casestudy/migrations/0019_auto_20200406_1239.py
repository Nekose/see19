# Generated by Django 3.0.4 on 2020-04-06 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('casestudy', '0018_auto_20200406_1233'),
    ]

    operations = [
        migrations.AddField(
            model_name='region',
            name='A70PLUSB',
            field=models.PositiveIntegerField(null=True, verbose_name='Aulation 65 and Older'),
        ),
        migrations.AddField(
            model_name='region',
            name='A75PLUSB',
            field=models.PositiveIntegerField(null=True, verbose_name='Aulation 65 and Older'),
        ),
        migrations.AddField(
            model_name='region',
            name='A80PLUSB',
            field=models.PositiveIntegerField(null=True, verbose_name='Aulation 65 and Older'),
        ),
        migrations.AddField(
            model_name='region',
            name='A85PLUSB',
            field=models.PositiveIntegerField(null=True, verbose_name='Aulation 65 and Older'),
        ),
    ]
