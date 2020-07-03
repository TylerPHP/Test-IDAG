from django.db import models
from datetime import datetime


class Images(models.Model):
    path_hash = models.CharField(max_length=150)
    add_date = models.DateTimeField(max_length=140, default=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    uploade_date = models.DateTimeField(max_length=140, default=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    def __str__(self):
        return self.name
