from django.db import models
from django.urls import reverse
from photo.fields import ThumbnailImageField # 커스텀 필드

class Album(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField('One Line Description', max_length=100,
                                   blank=True)
    
    class Meta:
        ordering = ('name',)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("photo:album_detail", args=(self.id, ))
    
class Photo(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    title = models.CharField('제목', max_length=30)
    description = models.TextField('사진 설명', blank=True)
    image = ThumbnailImageField(upload_to = 'photo/%Y/%m')
    upload_dt = models.DateTimeField('업로드 일', auto_now_add=True)

    class Meta:
        ordering = ('제목',)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("photo:photo_detail", args=(self.id,))    
    