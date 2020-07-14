from django.db import models

from datetime import datetime


class Images(models.Model):
    images = models.FileField(upload_to='images/')
    update_date = models.DateTimeField(max_length=140, default=datetime.now)

    class Meta:
        verbose_name = "Картинка"
        verbose_name_plural = "Картинки"
