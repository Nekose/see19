# Generated by Django 3.0.4 on 2020-04-06 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('casestudy', '0020_auto_20200406_1612'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='region',
            name='A04UNDERB',
        ),
        migrations.AddField(
            model_name='region',
            name='A65_69B',
            field=models.PositiveIntegerField(null=True, verbose_name='Population 65 to 69'),
        ),
        migrations.AddField(
            model_name='region',
            name='A70_74B',
            field=models.PositiveIntegerField(null=True, verbose_name='Population 70 to 74'),
        ),
        migrations.AddField(
            model_name='region',
            name='A75_79B',
            field=models.PositiveIntegerField(null=True, verbose_name='Population 75 to 79'),
        ),
        migrations.AddField(
            model_name='region',
            name='A80_84B',
            field=models.PositiveIntegerField(null=True, verbose_name='Population 80 to 84'),
        ),
    ]
