from django.shortcuts import render
from django.views import View
from ImagesApp.models import Images
from .forms import ImageForm
from django.core.files.storage import FileSystemStorage
import random


class ShowImage(View):
    """Класс предстваления"""
    def get(self, request):
        """Главная страница"""
        images = Images.objects.all()
        context = {'all_images': images}
        return render(request, 'ImagesApp/index.html', context)


class UploadImage(View):
    """Класс обновления изображений"""
    def get(self, request):
        """Отображение изображений"""
        img = request.GET.get("img")
        if not img:
            img = ''
        context = {'image': img}
        return render(request, 'ImagesApp/upload.html', context)

    def post(self, request):
        """Загрузка или обновление файла"""
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            if request.POST['name'] == '':
                form.save()
            else:
                m = Images(images=request.FILES)
                m.save()
        return render(request, 'ImagesApp/upload.html')

