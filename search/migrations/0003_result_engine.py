# Generated by Django 3.0.2 on 2020-01-04 23:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0002_auto_20200105_0232'),
    ]

    operations = [
        migrations.AddField(
            model_name='result',
            name='engine',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]
