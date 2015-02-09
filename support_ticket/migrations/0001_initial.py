# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import support_ticket.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='FileAttachment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('description', models.TextField()),
                ('file', models.FileField(upload_to=support_ticket.models.get_upload_path)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=120)),
                ('description', models.TextField()),
                ('reference_url', models.URLField(blank=True)),
                ('priority', models.CharField(default=b'NORMAL', max_length=6, choices=[(b'HIGH', b'High'), (b'NORMAL', b'Normal'), (b'LOW', b'Low')])),
                ('status', models.CharField(default=b'NEW', max_length=10, choices=[(b'NEW', b'New'), (b'OPEN', b'Open'), (b'REVIEW', b'Review'), (b'CLOSED', b'Closed'), (b'REOPENED', b'Reopened'), (b'DELETED', b'Deleted')])),
                ('owner', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Update',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('message', models.TextField()),
                ('ticket', models.ForeignKey(to='support_ticket.Ticket')),
                ('writer', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='fileattachment',
            name='ticket',
            field=models.ForeignKey(to='support_ticket.Ticket'),
            preserve_default=True,
        ),
    ]
