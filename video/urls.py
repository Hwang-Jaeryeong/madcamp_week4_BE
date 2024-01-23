from django.urls import path

from madcamp_week4_BE import settings
from .views import VideoUploadView
from django.conf.urls.static import static

urlpatterns = [
    path('upload/', VideoUploadView.as_view(), name='video-upload'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)