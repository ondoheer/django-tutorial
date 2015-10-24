# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wines', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grape',
            name='type',
            field=models.CharField(choices=[('red_wine', 'Red Wine'), ('white_wine', 'White Wine'), ('rose_wine', 'Rose Wine')], max_length=30),
        ),
    ]
