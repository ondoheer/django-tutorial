# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wines', '0003_auto_20151024_0948'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='grape',
            name='wines',
        ),
        migrations.RemoveField(
            model_name='wine',
            name='type',
        ),
        
        migrations.AddField(
            model_name='wine',
            name='type',
            field=models.ForeignKey(to='wines.Grape'),
        ),
    ]
