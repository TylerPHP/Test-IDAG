from django.urls import path
from ImagesApp.views import *

urlpatterns = [
    path('', ShowImage.as_view()),
    path('upload/', UploadImage.as_view()),
    # path('<str:image_hash>', ShowImage.as_view()),
]
