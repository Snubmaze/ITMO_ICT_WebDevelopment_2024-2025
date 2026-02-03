from django.contrib import admin
from .models import (
    Subject, Teacher, Classroom, SchoolClass, Student, Grade,
    WeekDay, TimeSlot, Schedule
)


admin.site.register(Subject)
admin.site.register(Teacher)
admin.site.register(Classroom)
admin.site.register(SchoolClass)
admin.site.register(Student)
admin.site.register(Grade)
admin.site.register(WeekDay)
admin.site.register(TimeSlot)
admin.site.register(Schedule)

