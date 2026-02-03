from django.db import models
from datetime import timedelta


class TimeSlot(models.Model):
    lesson_number = models.PositiveSmallIntegerField(unique=True)
    start_time = models.TimeField()
    end_time = models.TimeField()

    class Meta:
        constraints = [
            models.CheckConstraint(
                condition=models.Q(end_time__gt=models.F('start_time')),
                name='end_time_after_start_time',
            ),
            models.CheckConstraint(
                condition=models.Q(end_time__gt=models.F('start_time') + timedelta(minutes=45)),
                name='min_duration_45_minutes'
            )
        ]
    
    def __str__(self):
        return f'{self.lesson_number}: {self.start_time} - {self.end_time}'