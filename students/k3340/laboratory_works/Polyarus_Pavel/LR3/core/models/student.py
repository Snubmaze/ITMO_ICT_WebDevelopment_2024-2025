from django.db import models
from .school_class import SchoolClass


class Student(models.Model):
    GENDER_CHOICES = [
        ('M', 'Мужской'),
        ('F', 'Женский'),
    ]
    
    last_name = models.CharField(max_length=40)
    first_name = models.CharField(max_length=30)
    middle_name = models.CharField(max_length=30)

    gender = models.CharField(
        max_length=10,
        choices=GENDER_CHOICES
    )

    school_class = models.ForeignKey(
        SchoolClass,
        on_delete=models.CASCADE,
        related_name='students'
    )

    def __str__(self):
        return f'{self.last_name} {self.first_name} {self.middle_name}'
