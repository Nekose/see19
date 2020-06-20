# Generated by Django 3.0.4 on 2020-03-29 19:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('casestudy', '0008_auto_20200329_1656'),
    ]

    operations = [
        migrations.AddField(
            model_name='temperature',
            name='region',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='casestudy.Region'),
            preserve_default=False,
        ),
    ]
