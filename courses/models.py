from django.db import models
from django.core.exceptions import ValidationError


def validate_only_one_instance(obj):
    model = obj.__class__
    if (model.objects.count() > 0 and
                obj.id != model.objects.get().id):
        raise ValidationError("Can only create 1 %s instance. Delete or modify previous entry." % model.__name__)


class BtechCourses(models.Model):
    course_cirriculum = models.TextField()
    first_semester = models.TextField()
    second_semester = models.TextField()
    third_semester = models.TextField()
    fourth_semester = models.TextField()
    fifth_semester = models.TextField()
    sixth_semester = models.TextField()
    seventh_semester = models.TextField()
    seventh_department_elective_semester = models.TextField()
    eighth_semester = models.TextField()
    eighth_department_elective_semester = models.TextField()
    elective_courses_pdf_link = models.TextField(blank=True, null=True)

    def __str__(self):
        return "Btech Courses"

    def clean(self):
        validate_only_one_instance(self)

    class Meta:
        verbose_name_plural = "BtechCourses"


class MscCourses(models.Model):
    course_cirriculum = models.TextField()
    first_semester = models.TextField()
    second_semester = models.TextField()
    third_semester = models.TextField()
    fourth_semester = models.TextField()
    new_courses_pdf_link = models.TextField(blank=True, null=True)

    def __str__(self):
        return "Msc Courses"

    def clean(self):
        validate_only_one_instance(self)

    class Meta:
        verbose_name_plural = "MscCourses"


class PhdCourses(models.Model):
    supermolecular_chemistry = models.TextField()
    new_reagents_for_organic_synthesis = models.TextField()
    spectroscopic_techniques = models.TextField()
    art_in_organic_synthesis = models.TextField()
    bioanalytical_techniques = models.TextField()
    computation_chemistry = models.TextField()
    polymer_science_technology = models.TextField()
    application_glycochemistry = models.TextField()
    new_courses_pdf_link = models.TextField(blank=True, null=True)

    def __str__(self):
        return "Phd Courses"

    def clean(self):
        validate_only_one_instance(self)

    class Meta:
        verbose_name_plural = "PhdCourses"
