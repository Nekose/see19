# Generated by Django 3.0.4 on 2020-04-04 22:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('casestudy', '0013_delete_newcases'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='deaths',
            name='region',
        ),
        migrations.DeleteModel(
            name='Cases',
        ),
        migrations.DeleteModel(
            name='Deaths',
        ),
    ]
