from django.db import models

class Events(models.Model):
    ONGOING = 'ON'
    UPCOMING = 'UP'
    PAST = 'PA'
    STATUS = (
            (ONGOING, 'Ongoing'),
            (UPCOMING, 'Upcoming'),
            (PAST, 'Past')
    )
    topic = models.CharField(max_length=400)
    date = models.DateTimeField()
    speaker = models.CharField(max_length=200)
    status = models.CharField(
        max_length=2,
        choices=STATUS,
        default='UP'
    )
    additional_info = models.CharField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.topic

    class Meta:
        verbose_name_plural = "Events"
