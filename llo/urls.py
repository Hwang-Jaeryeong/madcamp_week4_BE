# urls.py
from django.urls import path
from .views import TeamLogoUpload

urlpatterns = [
    path('upload/', TeamLogoUpload.as_view(), name='team-logo-upload'),
    # 추가적인 URL 패턴 및 뷰는 필요에 따라 정의
]
