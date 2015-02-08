from django.db import models

# Create your models here.
from support_user.models import User


class Ticket(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    owner = models.ForeignKey(User)
    