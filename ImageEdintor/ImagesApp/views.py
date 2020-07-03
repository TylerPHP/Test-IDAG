from django.shortcuts import render
from django.views import View


class ShowImage(View):
    """Класс предстваления"""
    def get(self, request):
        """Главная страница"""
        return render(request, 'ImagesApp/index.html')


class UploadImage(View):
    """Класс обновления изображений"""
    def get(self, request):
        """Главная страница"""
        return render(request, 'ImagesApp/upload.html')
