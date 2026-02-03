from django.db import models
from .classroom import Classroom
from .school_class import SchoolClass
from .subject import Subject
from .teacher import Teacher
from .weekday import WeekDay
from .timeslot import TimeSlot


class Schedule(models.Model):
    school_class = models.ForeignKey(
        SchoolClass,
        on_delete=models.CASCADE,
        related_name='schedule'
    )

    subject = models.ForeignKey(
        Subject,
        on_delete=models.CASCADE,
        related_name='subject_schedule'
    )

    teacher = models.ForeignKey(
        Teacher,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='schedule'
    )
    
    classroom = models.ForeignKey(
        Classroom,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='classroom_schedule'
    )

    weekday = models.ForeignKey(
        WeekDay,
        on_delete=models.CASCADE,
        related_name='weekday_schedule'
    )

    timeslot = models.ForeignKey(
        TimeSlot,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='timeslot_schedule'
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['classroom', 'weekday', 'timeslot'],
                name='unique_classroom_per_slot'
            ),
            models.UniqueConstraint(
                fields=['teacher', 'weekday', 'timeslot'],
                name='unique_teacher_per_slot'
            ),
            models.UniqueConstraint(
                fields=['classroom', 'weekday', 'timeslot'],
                name='unique_class_per_slot'
            ),
        ]

    def __str__(self):
        return f'{self.school_class} | {self.weekday} | {self.timeslot}'

