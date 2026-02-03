from rest_framework import serializers
from core.models.schedule import Schedule

from .subject import SubjectSerializer
from .teacher import TeacherSerializer
from .classroom import ClassroomSerializer
from .weekday import WeekDaySerializer
from .timeslot import TimeSlotSerializer

from core.models import (
    Subject,
    Teacher,
    WeekDay,
    Classroom,
    TimeSlot
)


class ScheduleSerializer(serializers.ModelSerializer):
    subject = SubjectSerializer(read_only=True)
    teacher = TeacherSerializer(read_only=True)
    classroom = ClassroomSerializer(read_only=True)
    weekday = WeekDaySerializer(read_only=True)
    timeslot = TimeSlotSerializer(read_only=True)

    subject_id = serializers.PrimaryKeyRelatedField(
        queryset=Subject.objects.all(),
        source='subject',
        write_only=True
    )
    teacher_id = serializers.PrimaryKeyRelatedField(
        queryset=Teacher.objects.all(),
        source='teacher',
        write_only=True
    )
    classroom_id = serializers.PrimaryKeyRelatedField(
        queryset=Classroom.objects.all(),
        source='classroom',
        write_only=True
    )
    weekday_id = serializers.PrimaryKeyRelatedField(
        queryset=WeekDay.objects.all(),
        source='weekday',
        write_only=True
    )
    timeslot_id = serializers.PrimaryKeyRelatedField(
        queryset=TimeSlot.objects.all(),
        source='timeslot',
        write_only=True
    )

    class Meta:
        model = Schedule
        fields = [
            'id',
            'school_class',
            'subject',
            'subject_id',
            'teacher',
            'teacher_id',
            'classroom',
            'classroom_id',
            'weekday',
            'weekday_id',
            'timeslot',
            'timeslot_id',
        ]


    