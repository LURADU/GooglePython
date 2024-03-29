
from django.db import models


class Job(models.Model):
    type = models.CharField(max_length=11)
    url = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    description = models.TextField()
    how_to_apply = models.TextField()
    active = models.BooleanField(default=1)

    def __str__(self):
        return f"{self.title} - {self.description}"