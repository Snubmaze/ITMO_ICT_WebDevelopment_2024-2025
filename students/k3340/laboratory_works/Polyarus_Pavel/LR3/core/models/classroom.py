from django.db import models
from .subject import Subject


class Classroom(models.Model):
    nubmer = models.CharField(max_length=10, unique=True)

    is_sports_hall = models.BooleanField(default=False)

    specialized_subjects = models.ManyToManyField(
        Subject,
        blank=True,
        related_name='specialized_classrooms'
    )

    def __str__(self):
        return f'{self.nubmer}'
