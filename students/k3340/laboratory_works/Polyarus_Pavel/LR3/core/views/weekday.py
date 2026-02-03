from rest_framework.viewsets import ModelViewSet
from core.models.weekday import WeekDay
from core.serializers.weekday import WeekDaySerializer


class WeekDayViewSet(ModelViewSet):
    queryset = WeekDay.objects.all()
    serializer_class = WeekDaySerializer
