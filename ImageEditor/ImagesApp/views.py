from django.shortcuts import render
from django.views import View
from ImagesApp.models import Images
from .forms import ImageForm
from django.core.files.storage import FileSystemStorage
import random
from datetime import datetime


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
        print(form.errors)
        if form.is_valid():
            print('ok')
            form.save()
        # print(form)
        return render(request, 'ImagesApp/upload.html')

    # def post(self, request):
    #     """Обновление выбранного изображения по hash"""
    #     if request.method == 'POST' and request.FILES['newImage']:
    #         myfile = request.FILES['newImage']
    #         fs = FileSystemStorage()
    #         filename = fs.save(str(random.randint(1, 1000000)) + '.png', myfile)
    #         uploaded_file_url = fs.url(filename)
    #         return render(request, 'ImagesApp/upload.html', {
    #             'image': uploaded_file_url
    #         })
    #     return render(request, 'ImagesApp/upload.html')
