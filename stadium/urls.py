from django.urls import path
from .views import StadiumAPIView, StadiumUploadAPIView

urlpatterns = [
    path('', StadiumAPIView.as_view(), name='get-stadium'),
    path('upload/', StadiumUploadAPIView.as_view(), name='upload-stadium'),
]