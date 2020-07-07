from django.db import models
from datetime import datetime


class Images(models.Model):
    path_hash = models.CharField(max_length=150)
    add_date = models.DateTimeField(max_length=140, default=datetime.now)
    uploade_date = models.DateTimeField(max_length=140, default=datetime.now)

    def __str__(self):
        return self.path_hash

    class Meta:
        verbose_name = "Картинка"
        verbose_name_plural = "Картинки"
