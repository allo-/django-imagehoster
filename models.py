from django.db import models
from django.db.models.signals import pre_delete
from django.dispatch import receiver
import settings

assert hasattr(settings, "UPLOAD_DIR"), "you need to set UPLOAD_DIR (relative to MEDIA_URL) in settings"
assert len(settings.UPLOAD_DIR) and settings.UPLOAD_DIR[-1] == "/", "UPLOAD_DIR must have a trailing slash"

class Image(models.Model):
    date=models.DateTimeField(auto_now_add=True)
    image=models.ImageField(upload_to=settings.UPLOAD_DIR)

    def get_filename(self):
        return str(self.image.name).split("/")[-1]

@receiver(pre_delete, sender=Image)
def image_deleted(sender, instance, **kwargs):
    instance.image.delete()
