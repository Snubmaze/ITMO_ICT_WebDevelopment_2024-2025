from rest_framework.viewsets import ModelViewSet
from core.models.schedule import Schedule
from core.serializers.schedule import ScheduleSerializer
from rest_framework.exceptions import ValidationError


class ScheduleViewSet(ModelViewSet):
    serializer_class = ScheduleSerializer
    
    def get_queryset(self):
        queryset = Schedule.objects.select_related(
            'school_class',
            'teacher',
            'classroom',
            'weekday',
            'timeslot'
        )
        
        school_class_id = self.request.query_params.get('class_id')
        weekday_id = self.request.query_params.get('weekday_id')

        if not school_class_id:
            raise ValidationError({
                'school_class': 'Параметр school_class обязателен'
            })
        
        queryset = queryset.filter(school_class_id=school_class_id)

        if weekday_id:
            queryset = queryset.filter(weekday_id=weekday_id)

        return queryset


 