from django.db import models


class Ticket(models.Model):
    subject = models.CharField(max_length=200)
    body = models.CharField(max_length=200)
    priority = models.CharField(max_length=200, null=True)
