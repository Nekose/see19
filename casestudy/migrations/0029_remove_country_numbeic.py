# Generated by Django 3.0.4 on 2020-04-10 14:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('casestudy', '0028_country'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='country',
            name='numbeic',
        ),
    ]
