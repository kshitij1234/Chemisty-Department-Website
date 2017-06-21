from django.db import models

class Projects(models.Model):
    title = models.CharField(max_length=100)
    principal_investigator = models.TextField(max_length=200)
    sponsoring_agency = models.CharField(max_length=100)
    budget = models.CharField(max_length=20)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Projects"
