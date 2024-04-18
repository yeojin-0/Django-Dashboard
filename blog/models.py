from django.db import models
from django.urls import reverse
from taggit.managers import TaggableManager

class Post(models.Model):
    title = models.CharField(verbose_name='제목', max_length=50)
    slug = models.SlugField("SLUG", unique=True, allow_unicode=True, 
                                help_text="제목의 별칭")
    description = models.CharField('설명', max_length=100, blank=True,
                                   help_text="간단하게 설명할 문구, 빈칸가능")
    content = models.TextField('내용')
    create_dt = models.DateTimeField('생성일', auto_now=True)
    modify_dt = models.DateTimeField("수정일", auto_now=True)
    tags = TaggableManager(blank=True) # 추가

    # 메타데이터 설정
    class Meta:

        # admin 사이트에서 표시할 이름
        verbose_name = 'post'
        verbose_name_plural = 'posts' # 복수 별칭

        # 데이터베이스 테이블
        db_table = 'blog_posts'

        # 정렬 순서
        ordering=('-modify_dt',)
    
    def __str__(self):
        return self.title
    # URL
    def get_absolute_url(self):
        return reverse('blog:post_detail', args=(self.slug, ))
    
    # 이전/다음 게시물을 가져오기
    def get_previous(self):
        return self.get_previous_by_modify_dt()
    def get_next(self):
        return self.get_next_by_modify_dt()

"""
# Question과 Choice 구조와 같습니다.
class Comment(models.Model):
    # user
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment = models.CharField(max_length=200)
    # date ....
"""   