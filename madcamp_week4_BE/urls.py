
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('info/', include('info.urls')),
    path('llo/', include('llo.urls')),
    path('news/', include('news.urls')),
    path('video/', include('video.urls')),
    path('stadium/', include('home.urls')),
    path('community/', include('community.urls')),
]
