from django.db import models
import os
# Create your models here.

def get_image_path(instance, filename):
    return os.path.join("UserImages",type(instance).__name__,str(instance.email),filename)

class Designations(models.Model):
    designation = models.CharField(max_length=100,blank=False)

    def __str__(self):
        return self.designation

class Faculty(models.Model):
    name = models.CharField(max_length=100,blank=False)
    designation = models.ForeignKey('Designations')
    email = models.EmailField(primary_key=True)
    phone = models.CharField(max_length=12)
    profile_link = models.CharField(max_length=200)
    profile_picture = models.ImageField(upload_to=get_image_path,blank=True,null=True)

    def __str__(self):
        return self.name
