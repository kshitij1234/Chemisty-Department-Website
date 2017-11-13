from django.db import models
import os, datetime
import shutil
from research.models import CurrentResearch
from directory.models import Faculty as Fac


def get_image_path_phd(instance, filename):
    return os.path.join("PeopleApp", "static", "UserImages", type(instance).__name__, filename)


def get_image_path(instance, filename):
    return os.path.join("PeopleApp", "static", "UserImages", type(instance).__name__, str(instance.pk), filename)


class Designations(models.Model):
    designation = models.CharField(max_length=100, blank=False)

    def __str__(self):
        return self.designation

    class Meta:
        verbose_name_plural = "Designations"


class Faculty(models.Model):
    name = models.CharField(max_length=100, blank=False)
    designation = models.ForeignKey('Designations')
    additional_info = models.CharField(max_length=200, blank=True, null=True)
    directory = models.ForeignKey(Fac, on_delete=models.SET_NULL, blank=True, null=True)
    email = models.CharField(primary_key=True, max_length=50)
    profile_link = models.CharField(max_length=200, default="#")
    profile_picture = models.ImageField(upload_to=get_image_path, blank=True, null=True)
    research_areas = models.TextField(blank=True, null=True)
    list_position = models.IntegerField(default=1)
    phd = models.CharField(max_length=100, blank=True, null=True)
    fax = models.CharField(max_length=20, blank=True, null=True)
    google_scholar = models.CharField(max_length=200, blank=True, null=True)
    webpage = models.CharField(max_length=200, blank=True, null=True)
    # phd_students = models.TextField(blank=True, null=True)
    research_group = models.TextField(blank=True, null=True)
    former_research_group = models.TextField(blank=True, null=True)
    professional_experience = models.TextField(blank=True, null=True)
    awards_honors = models.TextField(blank=True, null=True)
    member_of_professional_bodies = models.TextField(blank=True, null=True)
    publications = models.TextField(blank=True, null=True)
    invited_talks = models.TextField(blank=True, null=True)
    conference_presentations = models.TextField(blank=True, null=True)
    conference_attended = models.TextField(blank=True, null=True)
    sponsored_projects = models.TextField(blank=True, null=True)
    teaching = models.TextField(blank=True, null=True)
    patents = models.TextField(blank=True, null=True)
    current_research = models.ManyToManyField(CurrentResearch, blank=True)

    def __str__(self):
        return self.name

    def delete(self, *args, **kwargs):
        # object is being removed from db, remove the file from storage first
        path = os.path.join("PeopleApp", "static", "UserImages", type(self).__name__, str(self.pk))
        if os.path.exists(path):
            shutil.rmtree(path)
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

    class Meta:
        ordering = ('name',)
        verbose_name_plural = "Faculty"


class Staff(models.Model):
    name = models.CharField(max_length=100, blank=False)
    designation = models.ForeignKey('Designations')
    email = models.CharField(primary_key=True, max_length=50)
    phone = models.CharField(max_length=12, blank=True, null=True)
    profile_picture = models.ImageField(upload_to=get_image_path, blank=True, null=True)

    def __str__(self):
        return self.name

    def delete(self, *args, **kwargs):
        # object is being removed from db, remove the file from storage first
        path = os.path.join("PeopleApp", "static", "UserImages", type(self).__name__, str(self.pk))
        if os.path.exists(path):
            shutil.rmtree(path)
        return super(Staff, self).delete(*args, **kwargs)

    def save(self, *args, **kwargs):
        # object is possibly being updated, if so, clean up.
        self.remove_on_image_update()
        return super(Staff, self).save(*args, **kwargs)

    def remove_on_image_update(self):
        try:
            # is the object in the database yet?
            obj = Staff.objects.get(pk=self.pk)
        except Staff.DoesNotExist:
            # object is not in db, nothing to worry about
            return
        # is the save due to an update of the actual image file?
        if obj.profile_picture and self.profile_picture and obj.profile_picture != self.profile_picture:
            # delete the old image file from the storage in favor of the new file
            obj.profile_picture.delete()

    def get_image_path(self):
        return str(self.profile_picture.url)[16:]

    class Meta:
        verbose_name_plural = "Staff"


class Batch(models.Model):
    batch = models.CharField(max_length=20, blank=False)

    def __str__(self):
        return self.batch

    class Meta:
        verbose_name_plural = "Batch"


class UndergraduateStudents(models.Model):
    rollno = models.CharField(max_length=12, primary_key=True)
    name = models.CharField(max_length=100, blank=False)
    batch = models.ForeignKey('Batch')

    def __str__(self):
        return self.rollno

    class Meta:
        verbose_name_plural = "UndergraduateStudents"


class MscStudents(models.Model):
    rollno = models.CharField(max_length=12, primary_key=True)
    name = models.CharField(max_length=100, blank=False)
    batch = models.ForeignKey('Batch')
    email = models.CharField(unique=True, max_length=50, blank=False)
    profile_picture = models.ImageField(upload_to=get_image_path, blank=True, null=True)

    def __str__(self):
        return self.rollno

    def delete(self, *args, **kwargs):
        # object is being removed from db, remove the file from storage first
        path = os.path.join("PeopleApp", "static", "UserImages", type(self).__name__, str(self.pk))
        if os.path.exists(path):
            shutil.rmtree(path)
        return super(MscStudents, self).delete(*args, **kwargs)

    def save(self, *args, **kwargs):
        # object is possibly being updated, if so, clean up.
        self.remove_on_image_update()
        return super(MscStudents, self).save(*args, **kwargs)

    def remove_on_image_update(self):
        try:
            # is the object in the database yet?
            obj = MscStudents.objects.get(pk=self.pk)
        except MscStudents.DoesNotExist:
            # object is not in db, nothing to worry about
            return
        # is the save due to an update of the actual image file?
        if obj.profile_picture and self.profile_picture and obj.profile_picture != self.profile_picture:
            # delete the old image file from the storage in favor of the new file
            obj.profile_picture.delete()

    def get_image_path(self):
        return str(self.profile_picture.url)[16:]

    class Meta:
        verbose_name_plural = "MscStudents"


class PhdStudents(models.Model):
    broadcast_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, blank=False)
    batch = models.ForeignKey('Batch')
    email = models.CharField(max_length=50, blank=True, null=True)
    profile_picture = models.ImageField(upload_to=get_image_path_phd, blank=True, null=True)

    # At first thought of making it as ForeignKey of Faculty model but what if a faculty leaves
    # and this particular student has already passed out ?
    # We would want to delete the faculty from our Faculty database but at the same time would want
    # to show the faculty as supervisor of this student.
    # It is only possible if this is an independent field.
    # On second thoughts making it a foreign key so that profile of faculty
    # can be visited from there itself. If faculty is no longer in institute,
    # it will simply be set to null, which can be updated to point to another faculty if needed.

    supervisor = models.ForeignKey('Faculty', on_delete=models.SET_NULL, blank=True, null=True)
    research = models.TextField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        # object is possibly being updated, if so, clean up.
        self.remove_on_image_update()
        return super(PhdStudents, self).save(*args, **kwargs)

    def remove_on_image_update(self):
        try:
            # is the object in the database yet?
            obj = PhdStudents.objects.get(pk=self.pk)
        except PhdStudents.DoesNotExist:
            # object is not in db, nothing to worry about
            return
        # is the save due to an update of the actual image file?
        if obj.profile_picture and self.profile_picture and obj.profile_picture != self.profile_picture:
            # delete the old image file from the storage in favor of the new file
            obj.profile_picture.delete()

    def get_image_path(self):
        return str(self.profile_picture.url)[16:]

    class Meta:
        verbose_name_plural = "PhdStudents"


class PhdAlumni(models.Model):
    name = models.CharField(max_length=100, blank=False)
    emails = models.CharField(max_length=300, blank=True, null=True)
    profile_picture = models.ImageField(upload_to=get_image_path_phd, blank=True, null=True)
    thesis_title = models.TextField(max_length=400, blank=True)
    thesis_link = models.CharField(max_length=200, blank=True, default="#")
    date_defended = models.DateField(blank=True, null=True)
    supervisor = models.ForeignKey('Faculty', on_delete=models.SET_NULL, blank=True, null=True)
    # phd_supervisor = models.CharField(max_length=100, blank=True)
    # phd_supervisor_link = models.CharField(max_length=200, blank=True, default="#")
    current_position = models.TextField(max_length=400, blank=True)
    current_supervisor = models.CharField(max_length=100, blank=True)
    current_supervisor_link = models.CharField(max_length=200, blank=True, default="#")
    extra_info = models.TextField(max_length=500, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        # object is possibly being updated, if so, clean up.
        self.remove_on_image_update()
        return super(PhdAlumni, self).save(*args, **kwargs)

    def remove_on_image_update(self):
        try:
            # is the object in the database yet?
            obj = PhdAlumni.objects.get(pk=self.pk)
        except PhdAlumni.DoesNotExist:
            # object is not in db, nothing to worry about
            return
        # is the save due to an update of the actual image file?
        if obj.profile_picture and self.profile_picture and obj.profile_picture != self.profile_picture:
            # delete the old image file from the storage in favor of the new file
            obj.profile_picture.delete()

    def get_image_path(self):
        return str(self.profile_picture.url)[16:]

    class Meta:
        verbose_name_plural = "PhdAlumni"


YEAR_CHOICES = []
for r in range(1980, 2031):
    YEAR_CHOICES.append((r, r))


class Publication(models.Model):
    year = models.IntegerField(choices=YEAR_CHOICES, default=datetime.datetime.now().year)
    faculty = models.ManyToManyField(Faculty, blank=False)
    matter = models.TextField(max_length=5000)

    def __str__(self):
        return "Entry "+str(self.id)

    class Meta:
        verbose_name_plural = "Publications"
