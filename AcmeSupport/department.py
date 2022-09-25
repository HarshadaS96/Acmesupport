from django.db import models
from django.contrib.auth.models import User


class Department(models.Model):
    Name = models.CharField(max_length=200,null=True)
    Description = models.CharField(max_length=200)
    created_by = models.ForeignKey(User, related_name='created_by_admin', on_delete=models.CASCADE,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    Last_updated_at = models.DateTimeField(auto_now=True)
