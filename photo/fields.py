import os
from PIL import Image
from django.db.models.fields.files import ImageField, ImageFieldFile

class ThumbnailImageField:
    def _add_thumb(s):
        parts = s.split(".")
        parts.insert(-1, "thumb")
        if parts[-1].lower() not in ['jpeg', 'jpg']:
            parts[-1] = 'jpg'
        return ".".join(parts)
    
    @property
    def thumb_path(self):
        return self._add_thumb(self.path)