# Generated by Django 3.0.4 on 2020-04-25 06:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('casestudy', '0044_auto_20200425_0446'),
    ]

    operations = [
        migrations.CreateModel(
            name='Travel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.PositiveSmallIntegerField(verbose_name='Year')),
                ('visitors', models.IntegerField(verbose_name='Visitors')),
                ('region', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='casestudy.Region')),
            ],
        ),
    ]
