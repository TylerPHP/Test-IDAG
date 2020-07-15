from django.db import models

from datetime import datetime
import random


# def images_directory_path(instance, filename):
#     # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
#     print(instance, filename)
#     return 'images/{0}.jpg'.format(random.randint(0, 1000000))


class Images(models.Model):
    images = models.FileField(upload_to='images/')
    update_date = models.DateTimeField(max_length=140, default=datetime.now)

    class Meta:
        verbose_name = "Картинка"
        verbose_name_plural = "Картинки"
