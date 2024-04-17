from django.contrib import admin
from django.urls import path, include
from config.view import HomeView

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', HomeView.as_view(), name='home'), # 추가
    path("bookmark/", include('bookmark.urls')),
    path("blog/", include('blog.urls')),
]
