# Generated by Django 3.0.2 on 2020-01-05 09:17

from django.db import migrations
import picklefield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0003_result_engine'),
    ]

    operations = [
        migrations.AlterField(
            model_name='result',
            name='engine',
            field=picklefield.fields.PickledObjectField(editable=False),
        ),
    ]
