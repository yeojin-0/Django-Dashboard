from typing import Any
from blog.models import Post
from django.views.generic import ListView, DetailView, TemplateView # 추가 
from django.views.generic.dates import ArchiveIndexView, YearArchiveView, MonthArchiveView, DayArchiveView
from django.views.generic.dates import TodayArchiveView

# ListView
class PostLV(ListView):
    model = Post
    template_name = 'blog/post_all.html'
    context_object_name = 'posts'
    paginate_by = 2

# DetailView    
class PostDV(DetailView):
    model = Post

# ArchiveView
class PostAV(ArchiveIndexView):
    model = Post
    date_field = 'modify_dt'    

# YearArchiveView
class PostYAV(YearArchiveView):
    model = Post
    date_field = 'modify_dt'
    make_object_list = True
    #month_format = %b # 디폴트 값      

# MonthArchiveView
class PostMAV(MonthArchiveView):
    model = Post
    date_field = 'modify_dt'      

# DayArchiveView
class PostDAV(DayArchiveView):
    model = Post
    date_field = 'modify_dt'      

# TodayArchiveView
class PostTAV(TodayArchiveView):
    model = Post
    date_field = 'modify_dt'      

class TagCloudTV(TemplateView):
    template_name = 'taggit/taggit_cloud.html'

class TaggedObjectLV(TemplateView):
    template_name = 'taggit/taggit_post_list.html'
    model = Post

    def get_queryset(self):
        return Post.objects.filter(tags__name=self.kwargs.get('tag'))
    
    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        context['tagname'] = self.kwargs['tag']
        return context
