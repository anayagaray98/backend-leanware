from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class Project(models.Model):

    name = models.CharField(max_length=200, blank=False)
    description = models.CharField(max_length=500, blank=False)

    def __str__(self):
        return self.name


class Report(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(default=datetime.now, blank=True)
    project = models.OneToOneField(Project, on_delete=models.CASCADE)

    def __str__(self):
        return self.user

