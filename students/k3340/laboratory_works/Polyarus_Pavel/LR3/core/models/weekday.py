from django.db import models


class WeekDay(models.Model):
    name = models.CharField(max_length=10, unique=True)
    order = models.PositiveSmallIntegerField(unique=True)

    def __str__(self):
        return self.name