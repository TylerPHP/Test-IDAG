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
        context = {'image': request.GET.get("img")}
        return render(request, 'ImagesApp/upload.html', context)

    def post(self, request):
        """Обновление выбранного изображения"""
        form = ImageForm(request.POST, request.FILES)

        if form.is_valid():
            if request.POST['name'] == '':
                print(form.errors)
                form.save()
            else:
                m = Images.objects.get(id=request.POST['id'])
                # m.images =
        return render(request, 'ImagesApp/upload.html')

