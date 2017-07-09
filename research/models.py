import os

from django.db import models


def get_image_path(self, file):
    return os.path.join("research", "static", "images", type(self).__name__, file)


class Projects(models.Model):
    title = models.CharField(max_length=100)
    principal_investigator = models.TextField(max_length=200)
    sponsoring_agency = models.CharField(max_length=100)
    budget = models.CharField(max_length=20)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Projects"


class ResearchAreas(models.Model):
    title = models.CharField(max_length=300)
    detail = models.TextField(max_length=600)
    picture = models.ImageField(upload_to=get_image_path, blank=True, null=True)
    picture_text = models.CharField(max_length=100)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        # object is possibly being updated, if so, clean up.
        self.remove_on_image_update()
        return super(ResearchAreas, self).save(*args, **kwargs)

    def remove_on_image_update(self):
        try:
            # is the object in the database yet?
            obj = ResearchAreas.objects.get(pk=self.pk)
        except ResearchAreas.DoesNotExist:
            # object is not in db, nothing to worry about
            return
        # is the save due to an update of the actual image file?
        if obj.picture and self.picture and obj.picture != self.picture:
            # delete the old image file from the storage in favor of the new file
            obj.picture.delete()

    def get_image_url(self):
        return str(self.picture.url)[15:]

    class Meta:
        verbose_name_plural = "Research Areas"
