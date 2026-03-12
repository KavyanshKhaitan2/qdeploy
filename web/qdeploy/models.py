from django.db import models
from typing import TYPE_CHECKING


# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    repo_url = models.URLField()
    deployed = models.BooleanField()
