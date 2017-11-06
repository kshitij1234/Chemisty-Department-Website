import os

from django.db import models


def get_image_path(self, file):
    return os.path.join("research", "static", "images", type(self).__name__, file)


class Projects(models.Model):
    title = models.CharField(max_length=200)
    principal_investigator = models.TextField(max_length=200)
    sponsoring_agency = models.CharField(max_length=100)
    budget = models.CharField(max_length=20)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Projects"


class ResearchAreas(models.Model):
    def number():
        no = ResearchAreas.objects.count()
        if no == None:
            return 1
        else:
            return no + 1

    object_no = models.IntegerField(unique=False, default=number)
    title = models.CharField(max_length=1000)
    detail = models.TextField(max_length=5000)
    picture = models.ImageField(upload_to=get_image_path, blank=True, null=True)
    picture_text = models.CharField(max_length=1000)

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

    def int_to_en(self):
        num = self.object_no
        d = { 0 : 'zero', 1 : 'one', 2 : 'two', 3 : 'three', 4 : 'four', 5 : 'five',
              6 : 'six', 7 : 'seven', 8 : 'eight', 9 : 'nine', 10 : 'ten',
              11 : 'eleven', 12 : 'twelve', 13 : 'thirteen', 14 : 'fourteen',
              15 : 'fifteen', 16 : 'sixteen', 17 : 'seventeen', 18 : 'eighteen',
              19 : 'nineteen', 20 : 'twenty',
              30 : 'thirty', 40 : 'forty', 50 : 'fifty', 60 : 'sixty',
              70 : 'seventy', 80 : 'eighty', 90 : 'ninety' }
        k = 1000
        m = k * 1000
        b = m * 1000
        t = b * 1000

        assert(0 <= num)

        if (num < 20):
            return d[num]

        if (num < 100):
            if num % 10 == 0: return d[num]
            else: return d[num // 10 * 10] + '-' + d[num % 10]

        if (num < k):
            if num % 100 == 0: return d[num // 100] + ' hundred'
            else: return d[num // 100] + ' hundred and ' + int_to_en(num % 100)

        if (num < m):
            if num % k == 0: return int_to_en(num // k) + ' thousand'
            else: return int_to_en(num // k) + ' thousand, ' + int_to_en(num % k)

        if (num < b):
            if (num % m) == 0: return int_to_en(num // m) + ' million'
            else: return int_to_en(num // m) + ' million, ' + int_to_en(num % m)

        if (num < t):
            if (num % b) == 0: return int_to_en(num // b) + ' billion'
            else: return int_to_en(num // b) + ' billion, ' + int_to_en(num % b)

        if (num % t == 0): return int_to_en(num // t) + ' trillion'
        else: return int_to_en(num // t) + ' trillion, ' + int_to_en(num % t)

        raise AssertionError('num is too large: %s' % str(num))

    class Meta:
        verbose_name_plural = "Research Areas"
