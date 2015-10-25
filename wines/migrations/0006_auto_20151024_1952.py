# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wines', '0005_auto_20151024_1001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wine',
            name='image',
            field=models.ImageField(upload_to='', blank=True, null=True),
        ),
    ]
