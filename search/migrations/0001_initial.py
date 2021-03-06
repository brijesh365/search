# Generated by Django 3.0.2 on 2020-01-04 19:52

from django.db import migrations, models
import django.db.models.deletion
import search.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Query',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('query', models.CharField(db_index=True, max_length=256)),
                ('status', models.CharField(choices=[('IN_PROGRESS', 'In Progress'), ('COMPLETED', 'Completed')], default='IN_PROGRESS', max_length=30)),
            ],
            options={
                'verbose_name': 'search',
                'verbose_name_plural': 'searches',
            },
            managers=[
                ('objects', search.manager.QueryManager()),
            ],
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('result', models.TextField()),
                ('query', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='search.Query')),
            ],
            options={
                'verbose_name': 'result',
                'verbose_name_plural': 'results',
            },
            managers=[
                ('objects', search.manager.ResultManager()),
            ],
        ),
    ]
