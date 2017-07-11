from django.db import models


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
