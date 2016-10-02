from __future__ import unicode_literals

from django.db import models


class Talk(models.Model):
	topic = models.CharField(max_length=200, unique=True)
	votes = models.IntegerField(default=0)