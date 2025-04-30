from django.db import models
from django.contrib.auth.models import User

class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateTimeField()

    def __str__(self):
        return self.title

    def confirmed_participants_count(self):
        return self.participations.filter(will_come=True).count()

class Participation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, related_name="participations", on_delete=models.CASCADE)
    will_come = models.BooleanField(default=False)

    class Meta:
        unique_together = ('user', 'event')
