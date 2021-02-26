from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Gst(models.Model):
    gst = models.IntegerField(null=True)

class Otp(models.Model):
    user_id = models.IntegerField(null=True)
    otp = models.IntegerField(null=True)