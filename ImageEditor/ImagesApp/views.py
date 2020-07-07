from django.shortcuts import render
from django.views import View
from ImagesApp.models import Images
from django.core.files.storage import FileSystemStorage


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
        """Обновление выбранного изображения по hash"""
        if request.method == 'POST' and request.FILES['newImage']:
            new_image = request.FILES['newImage']
            fs = FileSystemStorage()
            filename = fs.save(new_image.name, new_image)
        context = {'image': request.GET.get("img")}
        return render(request, 'ImagesApp/upload.html', context)
