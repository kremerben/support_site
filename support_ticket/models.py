import os
from django.db import models

# Create your models here.
from support_user.models import User


class Ticket(models.Model):

    PRIORITY_CHOICES = (
        ('HIGH', 'High'),
        ('NORMAL', 'Normal'),
        ('LOW', 'Low'),
    )
    STATUS_CHOICES = (
        ('NEW', 'New'),
        ('OPEN', 'Open'),
        ('REVIEW', 'Review'),
        ('CLOSED', 'Closed'),
        ('REOPENED', 'Reopened'),
        ('DELETED', 'Deleted'),

    )

    title = models.CharField(max_length=120)
    description = models.TextField()
    reference_url = models.URLField()
    owner = models.ForeignKey(User)
    priority = models.CharField(max_length=6, choices=PRIORITY_CHOICES,
                                default='NORMAL')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES,
                              default='NEW')
    created = models.DateTimeField(auto_now_add=True, null=True)


class Update(models.Model):
    ticket = models.ForeignKey(Ticket)
    message = models.TextField()
    created = models.DateTimeField(auto_now_add=True, null=True)
    


def get_upload_path(instance, filename):
    return os.path.join("files/{}".format(instance.owner.id), '%Y/%m', filename)


class FileAttachment(models.Model):
    ticket = models.ForeignKey(Ticket)
    description = models.TextField()
    file = models.FileField(upload_to=get_upload_path)

