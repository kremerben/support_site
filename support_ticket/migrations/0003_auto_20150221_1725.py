# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('support_ticket', '0002_auto_20150209_0233'),
    ]

    operations = [
        migrations.CreateModel(
            name='UpdateTicket',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(null=True, editable=False)),
                ('updated', models.DateTimeField(null=True, editable=False)),
                ('message', models.TextField()),
                ('ticket', models.ForeignKey(to='support_ticket.Ticket')),
                ('writer', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='update',
            name='ticket',
        ),
        migrations.RemoveField(
            model_name='update',
            name='writer',
        ),
        migrations.DeleteModel(
            name='Update',
        ),
        migrations.AddField(
            model_name='fileattachment',
            name='created',
            field=models.DateTimeField(null=True, editable=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='fileattachment',
            name='updated',
            field=models.DateTimeField(null=True, editable=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='ticket',
            name='created',
            field=models.DateTimeField(null=True, editable=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='ticket',
            name='updated',
            field=models.DateTimeField(null=True, editable=False),
            preserve_default=True,
        ),
    ]
