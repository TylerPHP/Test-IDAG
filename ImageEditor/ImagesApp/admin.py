from django.contrib import admin
from ImagesApp.models import Images


class ArticleAdmin(admin.ModelAdmin):
    """Добовление путей к изображениям через админку"""
    list_display = ("path_hash", "add_date", "uploade_date")


admin.site.register(Images, ArticleAdmin)
