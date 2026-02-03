from django.db import models
from .student import Student
from .subject import Subject


class Grade(models.Model):
    GRADE_CHOICES = [
        (2, '2 - Неудовлетворительно'),
        (3, '3 - Удовлетворительно'),
        (4, '4 - Хорошо'),
        (5, '5 - Отлично')
    ]
    
    QUARTER_CHOICES = [
        (1, 'I четверть'),
        (2, 'II четверть'),
        (3, 'III четверть'),
        (4, 'IV четверть'),
    ]
    
    value = models.PositiveSmallIntegerField(choices=GRADE_CHOICES)
    quarter = models.PositiveSmallIntegerField(choices=QUARTER_CHOICES)

    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
        related_name='grades'
    )

    subject = models.ForeignKey(
        Subject,
        on_delete=models.CASCADE,
        related_name='grades'
    )

    class Meta:
        unique_together = ('student', 'subject', 'quarter')

    def __str__(self):
        return f'{self.student} - {self.subject}: {self.value}'