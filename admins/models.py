from django.db import models

# Create your models here.
class Admins(models.Model):
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)
  nickname = models.CharField(max_length=255, null=True)

