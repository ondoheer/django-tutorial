# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wines', '0002_auto_20151024_0943'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grape',
            name='wines',
            field=models.ForeignKey(null=True, to='wines.Wine'),
        ),
    ]
