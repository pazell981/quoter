# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('view_quotes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='author',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='quote',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='quote',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
            preserve_default=True,
        ),
    ]
