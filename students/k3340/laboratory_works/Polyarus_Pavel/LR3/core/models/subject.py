from django.db import models


class Subject(models.Model):
    TYPE_CHOICES = [
        ('base', 'Базовый(ая)'),
        ('profile', 'Профильный(ая)')
    ]
    
    name = models.CharField(max_length=20)
    subject_type = models.CharField(
        max_length=10,
        choices=TYPE_CHOICES
    )

    class Meta:
        unique_together = ('name', 'subject_type')

    def __str__(self):
        return f'{self.name} {self.get_subject_type_display()}'
