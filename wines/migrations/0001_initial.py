# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Grape',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('type', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('stp_id', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Wine',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('vineyard', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
                ('year', models.IntegerField()),
                ('type', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=50)),
                ('image', jsonfield.fields.JSONField()),
                ('notes', models.TextField()),
                ('rating', models.IntegerField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='wines',
            field=models.ManyToManyField(to='wines.Wine'),
        ),
        migrations.AddField(
            model_name='grape',
            name='wines',
            field=models.ForeignKey(to='wines.Wine'),
        ),
    ]
