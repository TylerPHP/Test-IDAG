from django import forms
from .models import Images


class ImageForm(forms.ModelForm):
    """Загрузка изображений"""
    class Meta:
        model = Images
        fields = ['images', 'update_date', ]
