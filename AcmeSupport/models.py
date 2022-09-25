from django.db import models
from django.contrib.auth.models import User
from .department import Department
# Create your models here.


class Signup(models.Model):
    Name = models.CharField(max_length=200)
    Email = models.EmailField(max_length=200)
    Phone_number = models.CharField(max_length=15)
    password = models.CharField(max_length=200)
    department = models.ForeignKey(Department, on_delete=models.CASCADE,null=True)
    Role = models.CharField(max_length=200,null=True)
    Created_by = models.ForeignKey(User, related_name='created_by_user', on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    Last_updated_at = models.DateTimeField(auto_now=True)





# class Department(models.Model):
#     Name = models.CharField(max_length=200)
#     Description = models.CharField(max_length=200)
#     created_by = models.ForeignKey(User, related_name='created_by_user')
#     created_at = models.DateTimeField(auto_now_add=True)
#     Last_updated_at = models.DateTimeField(auto_now=True)


