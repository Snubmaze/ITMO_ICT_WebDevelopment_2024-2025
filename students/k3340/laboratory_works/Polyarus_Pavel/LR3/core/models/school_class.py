from django.db import models
from .teacher import Teacher


class SchoolClass(models.Model):
    grade = models.PositiveSmallIntegerField()
    letter = models.CharField(max_length=1)

    class_teacher = models.OneToOneField(
        Teacher,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='class_lead'
    )

    class Meta:
        unique_together = ('grade', 'letter')

    def __str__(self):
        return f'{self.grade}{self.letter}'
