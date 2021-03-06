from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    image = models.ImageField(upload_to='profile_images', blank=True, null=True)
    about = models.TextField(blank=True)
    company = models.CharField(max_length=120, blank=True)
    phone = models.CharField(max_length=50, blank=True)
    alt_phone = models.CharField(max_length=50, blank=True)

    def __unicode__(self):
        return u"{}".format(self.username)