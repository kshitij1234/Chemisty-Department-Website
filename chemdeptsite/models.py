import os
from django.db import models
# from django.core.exceptions import ValidationError
#
# def validate_only_one_instance(obj):
#     model = obj.__class__
#     if (model.objects.count() > 0 and
#             obj.id != model.objects.get().id):
#         raise ValidationError("Can only create 1 %s instance. Delete previous or modify it." % model.__name__)

def get_image_path(self, file):
    return os.path.join("chemdeptsite", "static", "images", type(self).__name__, file)

class HeadsDesk(models.Model):
    picture = models.ImageField(upload_to=get_image_path, blank=True, null=True)
    message = models.TextField()
    profile = models.TextField()

    def save(self, *args, **kwargs):
        # object is possibly being updated, if so, clean up.
        self.remove_on_image_update()
        return super(HeadsDesk, self).save(*args, **kwargs)

    def remove_on_image_update(self):
        try:
            # is the object in the database yet?
            obj = HeadsDesk.objects.get(pk=self.pk)
        except HeadsDesk.DoesNotExist:
            # object is not in db, nothing to worry about
            return
        # is the save due to an update of the actual image file?
        if obj.picture and self.picture and obj.picture != self.picture:
            # delete the old image file from the storage in favor of the new file
            obj.picture.delete()

    def get_image_url(self):
        return str(self.picture.url)[19:]

    # def clean(self):
    #     validate_only_one_instance(self)

    class Meta:
        verbose_name_plural = "HeadsDesk"

class NoticeBoard(models.Model):
    title = models.CharField(max_length=300, blank=False)
    body = models.CharField(max_length=300, blank=True, null=True)
    date = models.DateTimeField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "NoticeBoard"


class News(models.Model):
    title = models.CharField(max_length=300, blank=False)
    date = models.DateTimeField()
    more_info = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "News"



class QuickLinks(models.Model):
    title = models.CharField(max_length=300, blank=False)
    link = models.URLField()
    date = models.DateTimeField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "QuickLinks"
