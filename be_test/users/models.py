from django.db import models
from django.utils import timezone

# Create your models here.

class Member(models.Model):
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)
  email = models.EmailField(default="admin@localhost")
  created_at = models.DateTimeField(default=timezone.now)
  def __str__(self):
    return f"{self.firstname} {self.lastname}"