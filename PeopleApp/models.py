from django.db import models
import os
import shutil
# Create your models here.

def get_image_path(instance, filename):
    return os.path.join("PeopleApp", "static", "UserImages", type(instance).__name__, str(instance.pk), filename)

class Designations(models.Model):
    designation = models.CharField(max_length=100, blank=False)

    def __str__(self):
        return self.designation

class Faculty(models.Model):

    name = models.CharField(max_length=100, blank=False)
    designation = models.ForeignKey('Designations')
    additional_info = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField(primary_key=True)
    phone = models.CharField(max_length=12)
    profile_link = models.CharField(max_length=200, default="#")
    profile_picture = models.ImageField(upload_to=get_image_path, blank=True, null=True)
    research_areas = models.TextField(max_length=300, blank=True, null=True)

    def __str__(self):
        return self.name

    def delete(self, *args, **kwargs):
        # object is being removed from db, remove the file from storage first
        shutil.rmtree(os.path.join("PeopleApp", "static", "UserImages", type(self).__name__, str(self.pk)))
        return super(Faculty, self).delete(*args, **kwargs)

    def save(self, *args, **kwargs):
        # object is possibly being updated, if so, clean up.
        self.remove_on_image_update()
        return super(Faculty, self).save(*args, **kwargs)

    def remove_on_image_update(self):
        try:
            # is the object in the database yet?
            obj = Faculty.objects.get(pk=self.pk)
        except Faculty.DoesNotExist:
            # object is not in db, nothing to worry about
            return
        # is the save due to an update of the actual image file?
        if obj.profile_picture and self.profile_picture and obj.profile_picture != self.profile_picture:
            # delete the old image file from the storage in favor of the new file
            obj.profile_picture.delete()

    def get_image_path(self):
        return str(self.profile_picture.url)[16:]
