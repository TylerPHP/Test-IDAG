from django.urls import path
from ImagesApp.views import *

urlpatterns = [
    path('', ShowImage.as_view()),
    path('upload/', UploadImage.as_view()),
]
