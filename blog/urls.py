from django.urls import path, re_path
from blog import views

app_name = 'blog'
urlpatterns = [
    # /blog/
    path("", views.PostLV.as_view(), name="index"),

    # blog/post/ (same as /blog/) 리스트
    path("post/", views.PostLV.as_view(), name="post_list"),
    
    # 한글 슬러그를 처리
    re_path(r'^post/(?P<slug>[-\w]+)/$', views.PostDV.as_view(), name="post_detail"),
    

    # ====== 날짜 관련 제네릭 뷰 ====== 
    # /blog/archive/
    path("archive/", views.PostAV.as_view(), name="post_archive"),
    
    # /blog/archive/<년>/
    path("archive/<int:year>/", views.PostYAV.as_view(), name="post_year_archive"),
    
    # /blog/archive/<년>/<월>/``
    path("archive/<int:year>/<str:month>/", views.PostMAV.as_view(), name="post_month_archive"),
    
    # /blog/archive/<년>/<월>/<일>
    path("archive/<int:year>/<str:month>/<int:day>/", views.PostYAV.as_view(), name="post_day_archive"),
    
    # /blog/archive/<Today>
    path("archive/today/", views.PostTAV.as_view(), name="post_day_archive"),
]