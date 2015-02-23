# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('support_ticket', '0004_fileattachment_owner'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(null=True, editable=False)),
                ('updated', models.DateTimeField(null=True, editable=False)),
                ('message', models.TextField()),
                ('ticket', models.ForeignKey(to='support_ticket.Ticket')),
                ('user', models.ForeignKey(related_name='comments', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='updateticket',
            name='ticket',
        ),
        migrations.RemoveField(
            model_name='updateticket',
            name='writer',
        ),
        migrations.DeleteModel(
            name='UpdateTicket',
        ),
        migrations.AlterField(
            model_name='ticket',
            name='owner',
            field=models.ForeignKey(related_name='tickets', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
