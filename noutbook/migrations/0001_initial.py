# Generated by Django 4.2.3 on 2023-08-11 05:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NoutbooksModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(default='', max_length=200)),
                ('protcessor', models.CharField(default='', max_length=50)),
                ('ram', models.IntegerField()),
                ('ssd', models.IntegerField(default=0)),
                ('hdd', models.IntegerField(default=0)),
                ('price', models.FloatField()),
                ('buy_date', models.DateTimeField(default=datetime.datetime.now)),
            ],
            options={
                'db_table': 'noutbooks',
            },
        ),
    ]