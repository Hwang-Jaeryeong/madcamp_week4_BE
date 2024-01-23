from django.urls import path
from .views import StadiumAPIView, StadiumUpload

urlpatterns = [
    path('', StadiumAPIView.as_view(), name='get-stadium'),
    path('upload/', StadiumUpload.as_view(), name='stadium-upload'),
]

