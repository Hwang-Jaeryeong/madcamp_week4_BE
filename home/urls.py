from django.urls import path
from django.conf.urls.static import static
from madcamp_week4_BE import settings
from .views import StadiumAPIView, StadiumUpload

urlpatterns = [
    path('', StadiumAPIView.as_view(), name='get-stadium'),
    path('upload/', StadiumUpload.as_view(), name='stadium-upload'),
]


if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)