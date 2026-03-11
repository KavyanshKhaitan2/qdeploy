from django.db import models
from typing import TYPE_CHECKING


# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    repo = models.URLField()
    deployed = models.BooleanField()
