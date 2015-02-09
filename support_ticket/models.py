import os
from django.db import models
from datetime import datetime

# Create your models here.
from support_user.models import User


class TimeStamp(models.Model):
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    last_modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Ticket(TimeStamp):

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
    reference_url = models.URLField(blank=True)
    owner = models.ForeignKey(User)
    priority = models.CharField(max_length=6, choices=PRIORITY_CHOICES,
                                default='NORMAL')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES,
                              default='NEW')

    def get_last_update_datetime(self):
        most_recent_update = Update.objects.filter(ticket=self).latest('last_modified')
        return most_recent_update.last_modified

    def get_readable_date(self):
        return datetime.strftime(self.date_created, "%a, %b %d, %Y %H:%M")

    def __unicode__(self):
        return "{}: {} - created on {}".format(self.owner.username, self.title[:30], self.get_readable_date())


class Update(TimeStamp):
    ticket = models.ForeignKey(Ticket)
    message = models.TextField()
    writer = models.ForeignKey(User)

    def update_ticket_status(self, new_status):
        self.ticket.status = new_status
        self.ticket.save()
        return True

def get_upload_path(instance, filename):
    yearmonth = datetime.strftime(instance.ticket.date_created, "%Y/%m")
    return os.path.join("files/{}/{}".format(instance.ticket.owner.id, yearmonth), filename)


class FileAttachment(TimeStamp):
    ticket = models.ForeignKey(Ticket)
    description = models.TextField(blank=True)
    file = models.FileField(upload_to=get_upload_path)

