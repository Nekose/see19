# Generated by Django 3.0.4 on 2020-06-19 19:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('casestudy', '0061_auto_20200612_1320'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hospitalizations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(verbose_name='Date')),
                ('hospitalizations', models.FloatField(null=True, verbose_name='Count')),
                ('region', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='casestudy.Region')),
            ],
            options={
                'unique_together': {('date', 'region')},
            },
        ),
    ]
