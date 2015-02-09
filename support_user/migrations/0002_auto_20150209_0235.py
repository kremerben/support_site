# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('support_user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='alt_phone',
            field=models.CharField(max_length=50, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='user',
            name='company',
            field=models.CharField(max_length=120, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='user',
            name='phone',
            field=models.CharField(max_length=50, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user',
            name='about',
            field=models.TextField(default=1, blank=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='image',
            field=models.ImageField(default=1, upload_to=b'profile_images', blank=True),
            preserve_default=False,
        ),
    ]
