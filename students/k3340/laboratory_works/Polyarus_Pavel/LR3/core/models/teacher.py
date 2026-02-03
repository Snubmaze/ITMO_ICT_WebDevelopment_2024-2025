from django.db import models
from .classroom import Classroom
from .subject import Subject


class Teacher(models.Model):
    last_name = models.CharField(max_length=40)
    first_name = models.CharField(max_length=30)
    middle_name = models.CharField(max_length=30)

    assigned_classroom = models.ForeignKey(
        Classroom,
        on_delete=models.SET_NULL,
        blank=True, 
        null=True,
        related_name='assigned_teacher'
    )

    subjects = models.ManyToManyField(
        Subject,
        related_name='teachers',
    )

    def __str__(self):
        return f'{self.last_name} {self.first_name} {self.middle_name}'